# Generated by Django 5.1 on 2024-10-17 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0002_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='date',
        ),
    ]