# Generated by Django 3.2.12 on 2022-05-03 11:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_alter_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='previous',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 3, 16, 40, 26, 104410)),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 5, 3, 16, 40, 26, 103411)),
        ),
    ]
