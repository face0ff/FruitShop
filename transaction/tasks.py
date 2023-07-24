import datetime
import random

from celery import shared_task

from FruitShop.celery import app
from transaction.models import Fruit, Transaction


@app.task()
def buy(time):
    transaction = Transaction.objects.create()
    if time == 6:
        instance = Fruit.objects.get(name='Яблоки')
        try:
            price = 4
            item = random.randint(1, 10)
            instance.balance = instance.balance + item
            transaction.answer = 'SUCCESS'
            instance.save()
            transaction.quantity = item
            transaction.price = item * price
            print(f'Купили яблок {item}')
            print(f"Всего яблок {instance.balance}")
        except:
            transaction.answer = 'ERROR'
            print('Недостаточно средств')

    elif time == 9:
        instance = Fruit.objects.get(name='Бананы')
        try:
            price = 1
            item = random.randint(10, 20)
            instance.balance = instance.balance + item
            transaction.answer = 'SUCCESS'
            instance.save()
            transaction.quantity = item
            transaction.price = item * price
            print(f'Купили бананов {item}')
            print(f"Всего бананов {instance.balance}")
        except:
            transaction.answer = 'ERROR'
            print('Недостаточно средств')
    elif time == 12:
        instance = Fruit.objects.get(name='Ананасы')
        try:
            price = 3
            item = random.randint(1, 10)
            instance.balance = instance.balance + item
            transaction.answer = 'SUCCESS'
            instance.save()
            transaction.quantity = item
            transaction.price = item * price
            print(f'Купили ананасы {item}')
            print(f"Всего ананасы {instance.balance}")
        except:
            transaction.answer = 'ERROR'
            print('Недостаточно средств')
    else:
        instance = Fruit.objects.get(name='Персики')
        try:
            price = 2
            item = random.randint(5, 15)
            instance.balance = instance.balance + item
            transaction.answer = 'SUCCESS'
            instance.save()
            transaction.quantity = item
            transaction.price = item * price
            print(f'Купили Персики {item}')
            print(f"Всего Персики {instance.balance}")
        except:
            transaction.answer = 'ERROR'
            print('Недостаточно средств')
    print(f'{datetime.datetime.now()} - {transaction.answer}: Поставщик привёз товар "{instance.name}"(количество: {transaction.quantity}). Со счёта списано {transaction.price} USD, покупка завершена.')
    transaction.status = True
    transaction.fruit_id = instance
    transaction.save()

@app.task()
def sell(time):
    transaction = Transaction.objects.create()
    if time == 6:
        instance = Fruit.objects.get(name='Яблоки')
        try:
            price = 5
            transaction.answer = 'SUCCESS'
            item = random.randint(1, 10)
            instance.balance = instance.balance - item
            instance.save()
            transaction.quantity = item
            transaction.price = item * price
            print(f'Продали яблок {item}')
            print(f"Всего яблок {instance.balance}")
        except:
            transaction.answer = 'ERROR'
            print('Недостаточно яблок')
    elif time == 9:
        instance = Fruit.objects.get(name='Бананы')
        try:
            price = 2
            transaction.answer = 'SUCCESS'
            item = random.randint(10, 20)
            instance.balance = instance.balance - item
            instance.save()
            transaction.quantity = item
            transaction.price = item * price
            print(f'Продали бананов {item}')
            print(f"Всего бананов {instance.balance}")
        except:
            transaction.answer = 'ERROR'
            print('Недостаточно бананов')
    elif time == 12:
        instance = Fruit.objects.get(name='Ананасы')
        try:
            price = 4
            transaction.answer = 'SUCCESS'
            item = random.randint(1, 10)
            instance.balance = instance.balance - item
            instance.save()
            transaction.quantity = item
            transaction.price = item * price
            print(f'Продали ананасы {item}')
            print(f"Всего ананасы {instance.balance}")
        except:
            transaction.answer = 'ERROR'
            print('Недостаточно ананасов')
    else:
        instance = Fruit.objects.get(name='Персики')
        try:
            price = 3
            transaction.answer = 'SUCCESS'
            item = random.randint(5, 15)
            instance.balance = instance.balance - item
            instance.save()
            transaction.quantity = item
            transaction.price = item * price
            print(f'Продали персики {item}')
            print(f"Всего персиков {instance.balance}")
        except:
            transaction.answer = 'ERROR'
            print('Недостаточно персиков')
    print(f'{datetime.datetime.now()} - {transaction.answer}: Продажа товара "{instance.name}"(количество: {transaction.quantity}). К счёту добавлено {transaction.price} USD, продажа завершена.')
    transaction.status = False
    transaction.fruit_id = instance
    transaction.save()
