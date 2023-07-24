from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    pass
# Create your models here.
class CustomUser(AbstractBaseUser):
    username = models.CharField(unique=True, max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    objects = CustomUserManager()
    def __str__(self):
        return self.username