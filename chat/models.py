from django.db import models

# Create your models here.
class Chat(models.Model):
    date = models.DateField(auto_now_add=True)
    text = models.TextField('Шутка', max_length=400)
