# Generated by Django 3.2.7 on 2021-10-24 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0020_alter_play_play_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hand',
            name='hand_complete',
            field=models.BooleanField(default=False),
        ),
    ]