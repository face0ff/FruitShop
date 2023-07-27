import json

from channels.generic.websocket import AsyncWebsocketConsumer
from stock.tasks import check_stock_task

class CheckStockConsumer(AsyncWebsocketConsumer):
    print('tyt')
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        print(message)
        result = check_stock_task.delay(self.channel_name)  # Pass the channel_name to the task
        self.result_task_id = result.id

    async def send_progress(self, event):
        progress = event['progress']
        await self.send(text_data=json.dumps({
            'status': 'completed',
            'audit_progress': progress,
        }))



class ChangeStockConsumer(AsyncWebsocketConsumer):
    print('tyt')
    async def connect(self):
        await self.channel_layer.group_add('updates_stock', self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard('updates_stock', self.channel_name)

    async def updates_stock(self, event):
        data = event['data']
        await self.send(text_data=json.dumps({
            'type': 'updates_stock',
            'data': data,
        }))