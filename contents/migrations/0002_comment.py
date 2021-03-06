# Generated by Django 2.2.6 on 2020-05-30 21:00

from django.db import migrations, models
import django.db.models.deletion
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('image', pyuploadcare.dj.models.ImageField()),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='contents.Material')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
