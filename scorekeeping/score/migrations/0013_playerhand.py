# Generated by Django 3.2.7 on 2021-10-25 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0002_player_team'),
        ('score', '0012_alter_hand_play'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerHand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hand', models.ManyToManyField(to='score.Hand')),
                ('player', models.ManyToManyField(to='player.Player')),
            ],
        ),
    ]
