# Generated by Django 5.0.4 on 2024-07-01 10:01

import commerce.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.FloatField()),
                ('description', models.TextField(max_length=500)),
                ('image', models.ImageField(default='blog/default.jpg', upload_to=commerce.models.upload_to, verbose_name='Image')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('salesCount', models.IntegerField()),
                ('short_description', models.TextField(max_length=500)),
                ('stock', models.IntegerField(default=1)),
                ('Category', models.ManyToManyField(to='blog.category')),
                ('tag', models.ManyToManyField(to='blog.tag')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'commerce_product',
            },
        ),
    ]