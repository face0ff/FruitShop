import datetime
import json

from asgiref.sync import async_to_sync, sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from chat.models import Chat
from chat.views import print_joke


class ChatConsumer(AsyncWebsocketConsumer):
    print('tyt_chat')

    async def connect(self):
        await self.channel_layer.group_add('chat', self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard('chat', self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        print(message)

        # Send message to room group
        await self.channel_layer.group_send(
            'chat', {"type": "chat_message", "message": message}
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        user = self.scope['user']
        current_time = datetime.datetime.now().time()
        formatted_time = current_time.strftime('%H:%M:%S')
        await sync_to_async(Chat.objects.create)(sender=user.username, text=message, date=formatted_time)
        await self.send(text_data=json.dumps({"message": message, 'user': user.username, 'time': formatted_time}))
        # Send message to WebSocket

class JokeConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('joke', self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard('joke', self.channel_name)

    async def receive(self, text_data):
        pass
    async def send_joke(self, event):
        joke = event["joke"]
        current_time = datetime.datetime.now().time()
        formatted_time = current_time.strftime('%H:%M:%S')
        user = self.scope['user']
        await sync_to_async(Chat.objects.create)(sender="Joker", text=joke, date=formatted_time)
        await self.send(text_data=json.dumps({"joke": joke, "time": formatted_time}))