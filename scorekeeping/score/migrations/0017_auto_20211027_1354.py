# Generated by Django 3.2.7 on 2021-10-27 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('score', '0016_playplayer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playplayer',
            old_name='player',
            new_name='players',
        ),
        migrations.RenameField(
            model_name='playplayer',
            old_name='play',
            new_name='plays',
        ),
    ]
