from django.db import models

# Create your models here.
class Bank(models.Model):
    score = models.IntegerField('Банк', default=0)

class File(models.Model):
    file = models.FileField('Декларация', upload_to='file/')
