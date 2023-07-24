from django.db import models

# Create your models here.
class Bank(models.Model):
    score = models.IntegerField('Банк', default=0)
    file = models.FileField('Декларация', upload_to='file/')
