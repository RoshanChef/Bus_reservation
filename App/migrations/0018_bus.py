# Generated by Django 5.0.1 on 2024-04-16 06:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0017_rename_numtickets_ticket_numtickets_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agency', models.CharField(max_length=25)),
                ('busid', models.CharField(max_length=5)),
                ('price', models.IntegerField()),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.state')),
            ],
        ),
    ]
