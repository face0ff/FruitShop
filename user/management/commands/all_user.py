from django.contrib.auth.models import User
from django.core.management import BaseCommand

from user.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        if User.objects.count() == 0:
            username = 'admin'
            password = 'admin'
            user = User.objects.create_superuser(username=username, password=password)
            user.save()
            print('go')

        if User.objects.count() == 1:
            username = 'user'
            password = 'user'
            user = User.objects.create_user(username=username, password=password)
            user.save()
            print('go')
