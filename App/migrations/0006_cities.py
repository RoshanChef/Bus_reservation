# Generated by Django 5.0.1 on 2024-04-13 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_delete_cities'),
    ]

    operations = [
        migrations.CreateModel(
            name='cities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.TextField()),
            ],
        ),
    ]
