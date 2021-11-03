# Generated by Django 3.2.7 on 2021-10-25 03:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0024_delete_hand'),
        ('score', '0011_hand_play'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hand',
            name='play',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='play.play'),
        ),
    ]