from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


def updates_stock(stock_instance):
    channel_layer = get_channel_layer()
    data = {
        'id': stock_instance.id,
        'balance': stock_instance.balance,
        'last_transaction': stock_instance.last_transaction
    }
    async_to_sync(channel_layer.group_send)('updates_stock', {
        'type': 'updates_stock',
        'data': data,
    })