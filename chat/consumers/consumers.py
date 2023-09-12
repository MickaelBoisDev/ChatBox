from django.conf import settings
import urllib.parse
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
import json
from channels.generic.websocket import AsyncWebsocketConsumer
import logging
import jwt

logger = logging.getLogger(__name__)


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_id = f"room_{self.room_id}"

        query_string = self.scope.get("query_string", b"").decode("utf-8")
        query_params = urllib.parse.parse_qs(query_string)
        token = query_params.get("token", [None])[0]

        User = get_user_model()

        if token:
            try:
                decoded_data = jwt.decode(
                    token, settings.SECRET_KEY, algorithms=["HS256"])
            except jwt.ExpiredSignatureError:
                logger.error("JWT token has expired")
                await self.close()
                return
            except jwt.InvalidTokenError:
                logger.error("Invalid JWT token")
                await self.close()
                return

            try:
                self.user = await database_sync_to_async(User.objects.get)(id=decoded_data["user_id"])
            except User.DoesNotExist:
                logger.error("User does not exist")
                await self.close()
                return

        else:
            logger.error("No token provided")
            await self.close()
            return
    # Rejoindre la room
        await self.channel_layer.group_add(
            self.room_group_id,
            self.channel_name
        )

        await self.accept()

     # Récupérer et envoyer l'historique des messages
        messages = await get_room_messages(self.room_id)
        if messages:
            for message in messages:
                await self.send(text_data=json.dumps({
                    'username': message['user__username'],
                    'message': message['content'],
                    'timestamp': message['timestamp'].strftime('%Y-%m-%d %H:%M:%S'),
                }))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_id,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_content = text_data_json.get('text', '')
        try:
            user_id = int(text_data_json.get('user_id', ''))
        except ValueError:
            logger.error("Invalid user ID")
            return
        username = await get_username_by_id(user_id)
        if username:

            # Sauvegarder le message dans la base de données
            await save_message(self.room_id, user_id, message_content)

            # Envoyer le message à la room
            await self.channel_layer.group_send(
                self.room_group_id,
                {
                    'type': 'chat_message',
                    'message': message_content,
                    'username': username,
                }
            )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']  # Récupérez le username de l'événement

        # Envoyer le message à WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,  # Incluez le username dans le message WebSocket
        }))


@database_sync_to_async
def get_room_messages(room_id):
    from djangoChatApp.models import Message, Room
    try:
        room = Room.objects.get(id=room_id)
    except Room.DoesNotExist:
        logger.error(f"No room found with ID {room_id}")
        return []
    return list(Message.objects.filter(room=room).values('user__username', 'content', 'timestamp'))


@database_sync_to_async
def save_message(room_id, user_id, content):
    from django.contrib.auth import get_user_model
    from djangoChatApp.models import Message, Room
    User = get_user_model()

    try:
        room = Room.objects.get(id=room_id)  # Ici, j'ai changé name à id
    except Room.DoesNotExist:
        logger.error(f"No room found with ID {room_id}")
        return

    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        logger.error(f"No user found with ID {user_id}")
        return

    Message.objects.create(room=room, user=user, content=content)


@database_sync_to_async
def get_username_by_id(user_id):
    from django.contrib.auth import get_user_model
    User = get_user_model()
    try:
        print(user_id)
        user = User.objects.get(id=user_id)
        return user.username
    except User.DoesNotExist:
        logger.error(f"No user found with ID {user_id}")
        return None
