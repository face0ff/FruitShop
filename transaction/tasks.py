import datetime
import random

from celery import shared_task

from FruitShop.celery import app
from bank.models import Bank
from bank.views import edit_bank
from stock.models import Stock
from stock.views import updates_stock
from transaction.models import Transaction


@app.task()
def buy(id, count=None):
    transaction = Transaction.objects.create()
    score = Bank.objects.first().score
    if id == 1:
        instance = Stock.objects.get(id=id)
        price = 4
        if count:
            item = count
        else:
            item = random.randint(1, 10)
        if score >= item * price:
            instance.balance = instance.balance + item
            transaction.answer = 'SUCCESS'
        else:
            transaction.answer = 'ERROR'
        transaction.quantity = item
        transaction.price = item * price

    if id == 2:
        instance = Stock.objects.get(id=id)
        price = 1
        if count:
            item = count
        else:
            item = random.randint(10, 20)
        if score >= item * price:
            instance.balance = instance.balance + item
            transaction.answer = 'SUCCESS'
        else:
            transaction.answer = 'ERROR'
        transaction.quantity = item
        transaction.price = item * price

    if id == 3:
        instance = Stock.objects.get(id=id)
        price = 3
        if count:
            item = count
        else:
            item = random.randint(1, 10)
        if score >= item * price:
            instance.balance = instance.balance + item
            transaction.answer = 'SUCCESS'
        else:
            transaction.answer = 'ERROR'
        transaction.quantity = item
        transaction.price = item * price
    else:
        instance = Stock.objects.get(id=id)
        price = 2
        if count:
            item = count
        else:
            item = random.randint(5, 15)
        if score >= item * price:
            instance.balance = instance.balance + item
            transaction.answer = 'SUCCESS'
        else:
            transaction.answer = 'ERROR'
        transaction.quantity = item
        transaction.price = item * price

    if transaction.answer == 'SUCCESS':
        last_transaction = f'{datetime.datetime.now()} - {transaction.answer}: Поставщик привёз товар "{instance.name}"(количество: {transaction.quantity}). Со счёта списано {transaction.price} USD, покупка завершена.'
    else:
        last_transaction = f'{datetime.datetime.now()} - {transaction.answer}: Поставщик привёз товар "{instance.name}"(количество: {transaction.quantity}). Ошибка покупки!'
    instance.last_transaction = last_transaction
    updates_stock(instance)
    instance.save()
    transaction.status = True
    transaction.fruit_id = instance
    if transaction.answer == 'SUCCESS':
        edit_bank(transaction.price, True, last_transaction)
        transaction.save()
        return True
    else:
        transaction.save()
        return False

@app.task()
def sell(id, count=None):
    transaction = Transaction.objects.create()
    score = Bank.objects.first().score
    if id == 1:
        instance = Stock.objects.get(id=id)
        price = 5
        transaction.answer = 'SUCCESS'
        if count:
            item = count
        else:
            item = random.randint(1, 10)
        if instance.balance - item < 0:
            transaction.answer = 'ERROR'
        else:
            instance.balance = instance.balance - item
        transaction.quantity = item
        transaction.price = item * price
    if id == 2:
        instance = Stock.objects.get(id=id)
        price = 2
        transaction.answer = 'SUCCESS'
        if count:
            item = count
        else:
            item = random.randint(10, 20)
        if instance.balance - item < 0:
            transaction.answer = 'ERROR'
        else:
            instance.balance = instance.balance - item
        transaction.quantity = item
        transaction.price = item * price
    if id == 3:
        instance = Stock.objects.get(id=id)
        price = 4
        transaction.answer = 'SUCCESS'
        if count:
            item = count
        else:
            item = random.randint(1, 10)
        if instance.balance - item < 0:
            transaction.answer = 'ERROR'
        else:
            instance.balance = instance.balance - item
        transaction.quantity = item
        transaction.price = item * price
    else:
        instance = Stock.objects.get(id=id)
        price = 3
        transaction.answer = 'SUCCESS'
        if count:
            item = count
        else:
            item = random.randint(5, 15)
        if instance.balance - item < 0:
            transaction.answer = 'ERROR'
        else:
            instance.balance = instance.balance - item
        transaction.quantity = item
        transaction.price = item * price
    if transaction.answer == 'SUCCESS':
        last_transaction = f'{datetime.datetime.now()} - {transaction.answer}: Продажа товара "{instance.name}"(количество: {transaction.quantity}). К счёту добавлено {transaction.price} USD, продажа завершена.'
    else:
        last_transaction = f'{datetime.datetime.now()} - {transaction.answer}: Продажа товара "{instance.name}"(количество: {transaction.quantity}). Ошибка продажи.'
    instance.last_transaction = last_transaction
    updates_stock(instance)
    instance.save()
    transaction.status = False
    transaction.fruit_id = instance
    if transaction.answer == 'SUCCESS':
        edit_bank(transaction.price, False, last_transaction)
        transaction.save()
        return True
    else:
        transaction.save()
        return False
