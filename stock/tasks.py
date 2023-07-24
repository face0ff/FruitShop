import time

from celery import shared_task

from FruitShop.celery import app


@app.task(queue='test')
def check_stock_task():
    print('taska pohla')
    execution_time = "uspehniy uspeh"
    return execution_time