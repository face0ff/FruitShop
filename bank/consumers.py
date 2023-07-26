import json

from channels.generic.websocket import AsyncWebsocketConsumer
from stock.tasks import check_stock_task

class ChangeBankConsumer(AsyncWebsocketConsumer):
    print('tyt')
    async def connect(self):
        await self.channel_layer.group_add('updates', self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard('updates', self.channel_name)

    async def update_bank(self, event):
        data = event['data']
        await self.send(text_data=json.dumps({
            'type': 'update_bank',
            'data': data,
        }))

