# Generated by Django 2.1.15 on 2020-10-11 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Canteen', '0006_auto_20201011_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='contact_no',
            field=models.CharField(max_length=20),
        ),
    ]
