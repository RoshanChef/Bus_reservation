# Generated by Django 5.0.1 on 2024-04-16 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0025_remove_ticket_busid'),
    ]

    operations = [
        migrations.DeleteModel(
            name='bus',
        ),
    ]
