# Generated by Django 5.0.4 on 2024-05-27 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_user_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='max_otp_out',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='max_otp_try',
            field=models.CharField(default=3, max_length=2),
        ),
        migrations.AddField(
            model_name='user',
            name='otp',
            field=models.CharField(default='', max_length=4),
        ),
        migrations.AddField(
            model_name='user',
            name='otp_expiry',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
