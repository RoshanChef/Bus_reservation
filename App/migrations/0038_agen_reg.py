# Generated by Django 5.0.1 on 2024-04-17 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0037_delete_agen_reg'),
    ]

    operations = [
        migrations.CreateModel(
            name='agen_reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('agen_name', models.CharField(max_length=30)),
                ('number', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=100)),
                ('password', models.CharField(default='1', max_length=25)),
            ],
        ),
    ]
