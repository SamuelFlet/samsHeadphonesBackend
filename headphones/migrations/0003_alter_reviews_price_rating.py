# Generated by Django 3.2.12 on 2022-03-21 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('headphones', '0002_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='price_rating',
            field=models.IntegerField(default=0),
        ),
    ]
