# Generated by Django 5.0.4 on 2024-07-03 06:48

import commerce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='user_id',
        ),
        migrations.AddField(
            model_name='product',
            name='price_id',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='product',
            name='price_id_eur',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='product',
            name='price_id_gbp',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to=commerce.models.upload_to, verbose_name='Image'),
        ),
    ]
