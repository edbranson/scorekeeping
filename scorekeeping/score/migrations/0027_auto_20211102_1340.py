# Generated by Django 3.2.7 on 2021-11-02 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0027_auto_20211102_1340'),
        ('score', '0026_auto_20211102_1306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mmplayer',
            name='players',
        ),
        migrations.RemoveField(
            model_name='playhand',
            name='hand',
        ),
        migrations.RemoveField(
            model_name='playhand',
            name='mmhand',
        ),
        migrations.RemoveField(
            model_name='playplayer',
            name='mmplayer',
        ),
        migrations.RemoveField(
            model_name='playplayer',
            name='player',
        ),
        migrations.DeleteModel(
            name='MMHand',
        ),
        migrations.DeleteModel(
            name='MMPlayer',
        ),
        migrations.DeleteModel(
            name='PlayHand',
        ),
        migrations.DeleteModel(
            name='PlayPlayer',
        ),
    ]