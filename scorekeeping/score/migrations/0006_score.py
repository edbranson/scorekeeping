# Generated by Django 3.2.7 on 2021-10-22 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('play', '0014_playerhand'),
        ('game', '0001_initial'),
        ('player', '0002_player_team'),
        ('score', '0005_delete_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('game', models.ManyToManyField(to='game.Game')),
                ('hand', models.ManyToManyField(to='play.Hand')),
                ('play', models.ManyToManyField(to='play.Play')),
                ('player', models.ManyToManyField(to='player.Player')),
            ],
        ),
    ]
