# Generated by Django 5.0.1 on 2024-04-16 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0022_bus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bus',
            name='state',
        ),
        migrations.DeleteModel(
            name='ticket',
        ),
        migrations.DeleteModel(
            name='bus',
        ),
    ]
