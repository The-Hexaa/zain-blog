# Generated by Django 5.0.4 on 2024-07-03 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_peremium',
            field=models.BooleanField(default=False),
        ),
    ]
