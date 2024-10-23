# Generated by Django 5.1.2 on 2024-10-23 11:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_tweetbox', '0004_alter_tweet_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='text',
            field=models.TextField(validators=[django.core.validators.MaxLengthValidator(280)]),
        ),
    ]
