# Generated by Django 2.2.6 on 2020-05-29 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_auto_20200530_0456'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='transaction_id',
        ),
        migrations.AddField(
            model_name='order',
            name='secret_id',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
