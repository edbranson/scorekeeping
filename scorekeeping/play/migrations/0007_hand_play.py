# Generated by Django 3.2.7 on 2021-10-22 03:47

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0006_hand'),
    ]

    operations = [
        migrations.AddField(
            model_name='hand',
            name='play',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.PROTECT, to='play.play'),
        ),
    ]
