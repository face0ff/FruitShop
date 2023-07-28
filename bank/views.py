from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.shortcuts import render

from bank.models import Bank


# Create your views here.
def edit_bank(price, status, last_transaction=None):
    bank_score = Bank.objects.first()
    if status:
        bank_score.score = bank_score.score - price
    else:
        bank_score.score = bank_score.score + price

    bank_score.save()

    channel_layer = get_channel_layer()
    data = {
        'score': bank_score.score,
        'transaction': last_transaction
    }
    async_to_sync(channel_layer.group_send)('updates', {
        'type': 'update_bank',
        'data': data,
    })

