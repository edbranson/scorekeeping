# Generated by Django 3.2.7 on 2021-10-24 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_alter_game_rules_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='rules_link',
            field=models.URLField(default=None, max_length=40),
        ),
        migrations.AlterField(
            model_name='game',
            name='rules_text',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
