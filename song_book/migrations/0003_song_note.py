# Generated by Django 3.2.5 on 2021-08-23 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song_book', '0002_song_list_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='note',
            field=models.TextField(default='Click here to add notes...'),
        ),
    ]