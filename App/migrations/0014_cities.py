# Generated by Django 5.0.1 on 2024-04-14 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0013_delete_cities_alter_ticket_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='cities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=25)),
                ('seats', models.IntegerField()),
            ],
        ),
    ]
