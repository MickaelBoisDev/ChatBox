from channels.db import database_sync_to_async
import json
from channels.generic.websocket import AsyncWebsocketConsumer
import logging

logger = logging.getLogger(__name__)

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"chat_{self.room_name}"

        # Rejoindre la room
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # Récupérer et envoyer l'historique des messages
        messages = await get_room_messages(self.room_name)
        for message in messages:
            await self.send(text_data=json.dumps({
                'username': message['user__username'],
                'message': message['content'],
                'timestamp': message['timestamp'].strftime('%Y-%m-%d %H:%M:%S'),
            }))

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_content = text_data_json.get('message', '')
        username = text_data_json.get('username', '')  # Assurez-vous que le username est envoyé par le client

        # Sauvegarder le message dans la base de données
        await save_message(self.room_name, username, message_content)

        # Envoyer le message à la room
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message_content,
                'username': username,  # Transmettez le username pour l'inclure dans le message envoyé à `chat_message`
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
def get_room_messages(room_name):
    from djangoChatApp.models import Message, Room  # Déplacez l'importation des modèles ici
    room = Room.objects.get(name=room_name)
    return Message.objects.filter(room=room).values('user__username', 'content', 'timestamp')

@database_sync_to_async
def save_message(room_name, username, content):
    from django.contrib.auth import get_user_model  # Déplacez l'importation du modèle User ici
    from djangoChatApp.models  import Message, Room  # Déplacez l'importation des modèles ici
    User = get_user_model()
    room = Room.objects.get(name=room_name)
    user = User.objects.get(username=username)
    Message.objects.create(room=room, user=user, content=content)