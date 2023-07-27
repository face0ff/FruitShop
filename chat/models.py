from django.db import models

# Create your models here.
class Chat(models.Model):
    sender = models.CharField('Имя', max_length=100, default='user')
    date = models.CharField('Время', max_length=100)
    text = models.TextField('Шутка', max_length=400)
