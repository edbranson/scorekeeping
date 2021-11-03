# Generated by Django 3.2.7 on 2021-11-02 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0012_game_rules_link'),
        ('play', '0025_auto_20211102_1228'),
        ('player', '0002_player_team'),
        ('score', '0024_auto_20211031_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='game',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='game.game'),
        ),
        migrations.AlterField(
            model_name='score',
            name='hand',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='score.hand'),
        ),
        migrations.AlterField(
            model_name='score',
            name='play',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='play.play'),
        ),
        migrations.AlterField(
            model_name='score',
            name='player',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='player.player'),
        ),
    ]