# Generated by Django 5.0.1 on 2024-04-18 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0050_alter_order_orderid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='busid',
        ),
    ]
