# Generated by Django 3.2.12 on 2022-04-19 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_order_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address1',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
        migrations.AddField(
            model_name='customer',
            name='address2',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
        migrations.AddField(
            model_name='customer',
            name='address3',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(blank=True, default='1234567890', max_length=50),
        ),
    ]