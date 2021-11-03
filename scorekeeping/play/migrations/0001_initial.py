# Generated by Django 3.2.7 on 2021-10-21 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Play',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('location', models.CharField(max_length=30)),
                ('play_complete', models.BooleanField(default=False)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='game.game')),
            ],
        ),
    ]
