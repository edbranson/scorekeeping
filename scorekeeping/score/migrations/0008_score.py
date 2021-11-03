# Generated by Django 3.2.7 on 2021-10-25 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('game', '0012_game_rules_link'),
        ('player', '0002_player_team'),
        ('play', '0022_delete_score'),
        ('score', '0007_delete_score'),
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