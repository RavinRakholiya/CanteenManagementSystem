# Generated by Django 2.1.15 on 2020-10-11 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Canteen', '0009_auto_20201011_1852'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='order_id',
            new_name='orders_id',
        ),
    ]