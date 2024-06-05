# Generated by Django 5.0.4 on 2024-05-28 12:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(default='00000000000', max_length=14, validators=[django.core.validators.RegexValidator(message='Must be start with +92', regex='^\\+92\\d{10}')]),
        ),
    ]