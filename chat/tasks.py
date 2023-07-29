import datetime

from asgiref.sync import async_to_sync, sync_to_async
from channels.layers import get_channel_layer

from FruitShop.celery import app
from chat.models import Chat
from chat.views import print_joke


@app.task(queue='joke', bind=True)
def task_print_joke(self):
    print('joke')
    current_time = datetime.datetime.now().time()
    formatted_time = current_time.strftime('%H:%M:%S')
    channel_layer = get_channel_layer()
    joke = async_to_sync(print_joke)()
    if type(joke) is list:
        joke = f'{joke[0]} >>> {joke[1]}'
    else:
        joke = str(joke)
    async_to_sync(channel_layer.group_send)('joke', {
        'type': 'send_joke',
        'joke': joke,
        'formatted_time': formatted_time
    })
    Chat.objects.create(sender="Joker", text=joke, date=formatted_time)
    task_print_joke.apply_async(countdown=len(joke))