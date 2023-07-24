from django.db import models

from stock.models import Stock


# Create your models here.

# class Fruit(models.Model):
#     name = models.CharField('Название фрукта', max_length=10)
#     balance = models.PositiveIntegerField('Остаток', default=0)


class Transaction(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    answer = models.CharField('Ответ', max_length=10)
    quantity = models.PositiveIntegerField('Количество', default=0)
    price = models.PositiveIntegerField('Цена', default=0)
    status = models.BooleanField(null=True)
    fruit_id = models.ForeignKey(Stock, on_delete=models.CASCADE, null=True)


