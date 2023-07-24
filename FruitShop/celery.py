import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FruitShop.settings")
app = Celery('FruitShop', backend='redis')
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'add-every-6-seconds_buy': {
        'task': 'transaction.tasks.buy',
        'schedule': 6,
        'options': {'queue': 'buy'},
        'args': (6,),
    },
    'add-every-9-seconds_buy': {
        'task': 'transaction.tasks.buy',
        'schedule': 9,
        'options': {'queue': 'buy'},
        'args': (9,),
    },
    'add-every-12-seconds_buy': {
        'task': 'transaction.tasks.buy',
        'schedule': 12,
        'options': {'queue': 'buy'},
        'args': (12,),
    },
    'add-every-15-seconds_buy': {
        'task': 'transaction.tasks.buy',
        'schedule': 15,
        'options': {'queue': 'buy'},
        'args': (15,),
    },
    'add-every-6-seconds_sell': {
        'task': 'transaction.tasks.sell',
        'schedule': 6,
        'options': {'queue': 'sell'},
        'args': (6,),
    },
    'add-every-9-seconds_sell': {
        'task': 'transaction.tasks.sell',
        'schedule': 9,
        'options': {'queue': 'sell'},
        'args': (9,),
    },
    'add-every-12-seconds_sell': {
        'task': 'transaction.tasks.sell',
        'schedule': 12,
        'options': {'queue': 'sell'},
        'args': (12,),
    },
    'add-every-15-seconds_sell': {
        'task': 'transaction.tasks.sell',
        'schedule': 15,
        'options': {'queue': 'sell'},
        'args': (15,),
    },
}

app.conf.timezone = 'UTC'
