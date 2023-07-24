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
        result = check_stock_task.delay()

        execution_time = result.get()
        print(execution_time)
        await self.send(text_data=json.dumps({
            'status': 'completed',
            'execution_time': execution_time,
        }))