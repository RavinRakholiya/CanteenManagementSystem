# Generated by Django 2.1.15 on 2020-10-11 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Canteen', '0011_auto_20201011_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='order_status',
            field=models.CharField(default='unserved', max_length=10),
        ),
    ]
