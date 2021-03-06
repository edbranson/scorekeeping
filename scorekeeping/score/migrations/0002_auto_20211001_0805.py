# Generated by Django 3.2.7 on 2021-10-01 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0001_initial'),
        ('game', '0001_initial'),
        ('score', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='player',
        ),
        migrations.RemoveField(
            model_name='score',
            name='team',
        ),
        migrations.AlterField(
            model_name='score',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.game'),
        ),
        migrations.AlterField(
            model_name='score',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player.player'),
        ),
        migrations.DeleteModel(
            name='Game',
        ),
        migrations.DeleteModel(
            name='Player',
        ),
        migrations.DeleteModel(
            name='Team',
        ),
    ]
