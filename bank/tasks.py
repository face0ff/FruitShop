# import time
#
# from asgiref.sync import async_to_sync
# from channels.layers import get_channel_layer
#
# from FruitShop.celery import app
#
#
# @app.task(queue='test')
# def check_stock_task(channel_name):
#     print('taaaak')
#     channel_layer = get_channel_layer()
#     async_to_sync(channel_layer.send)(channel_name, {
#         'type': 'send_progress',
#         'progress': 0,
#     })
#     for test in range(1, 101):
#         print(test)
#         async_to_sync(channel_layer.send)(channel_name, {
#             'type': 'send_progress',
#             'progress': test,
#         })
#         time.sleep(0.1)
