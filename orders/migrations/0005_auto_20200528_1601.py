# Generated by Django 2.2.6 on 2020-05-28 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_order_resolve'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='resolve',
            field=models.CharField(max_length=30),
        ),
    ]
