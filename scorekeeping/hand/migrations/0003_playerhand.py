# Generated by Django 3.2.7 on 2021-10-22 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0002_player_team'),
        ('hand', '0002_remove_hand_player'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerHand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hand', models.ManyToManyField(to='hand.Hand')),
                ('player', models.ManyToManyField(to='player.Player')),
            ],
        ),
    ]