# Generated by Django 5.0.1 on 2024-04-16 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0031_ticket_stateid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bus',
            name='state',
        ),
        migrations.DeleteModel(
            name='state',
        ),
    ]
