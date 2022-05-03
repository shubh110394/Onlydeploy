# Generated by Django 3.2.12 on 2022-05-03 11:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_auto_20220503_1640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='time',
        ),
        migrations.RemoveField(
            model_name='previous',
            name='date',
        ),
        migrations.RemoveField(
            model_name='previous',
            name='time',
        ),
        migrations.AddField(
            model_name='order',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 3, 16, 45, 52, 152168)),
        ),
        migrations.AddField(
            model_name='previous',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 3, 16, 45, 52, 153168)),
        ),
    ]