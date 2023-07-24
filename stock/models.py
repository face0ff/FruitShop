from django.db import models

# Create your models here.
class Stock(models.Model):
    name = models.CharField('Название', max_length=10)
    quantity = models.PositiveIntegerField('Количество', default=0)
    last_transaction = models.CharField('Последняя транзакция', max_length=100)
