# Generated by Django 3.2.19 on 2023-07-24 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='file/', verbose_name='Декларация')),
            ],
        ),
        migrations.RemoveField(
            model_name='bank',
            name='file',
        ),
    ]
