# chat/consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer
import logging

# daphne djangoChatApp.asgi:application
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

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        logger.debug(f"Received WebSocket data: {text_data_json}")
        message = text_data_json.get('message', '')
        # Envoyer le message à la room.
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    async def chat_message(self, event):
        message = event['message']
        logger.info("Message reçu: %s", event)
        # Envoyer le message à WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
