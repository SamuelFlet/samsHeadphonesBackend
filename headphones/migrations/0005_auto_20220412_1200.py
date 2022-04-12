# Generated by Django 3.2.12 on 2022-04-12 16:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('headphones', '0004_auto_20220325_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='reviews',
            name='title',
            field=models.TextField(default='Default Title'),
        ),
    ]