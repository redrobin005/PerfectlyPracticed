# Generated by Django 3.2.5 on 2021-08-12 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song_book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='list_index',
            field=models.IntegerField(default=0),
        ),
    ]
