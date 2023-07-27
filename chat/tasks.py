from asgiref.sync import async_to_sync, sync_to_async
from channels.layers import get_channel_layer

from FruitShop.celery import app
from chat.models import Chat
from chat.views import print_joke


@app.task(queue='joke', bind=True)
def task_print_joke(self):
    print('joke')
    channel_layer = get_channel_layer()
    joke = async_to_sync(print_joke)()
    if type(joke) is list:
        joke = f'{joke[0]} >>> {joke[1]}'
    else:
        joke = str(joke)
    async_to_sync(channel_layer.group_send)('joke', {
        'type': 'send_joke',
        'joke': joke,
    })

    task_print_joke.apply_async(countdown=len(joke))