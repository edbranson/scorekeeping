# Generated by Django 3.2.7 on 2021-10-24 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_alter_game_rules_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='rules_text',
            field=models.CharField(max_length=200),
        ),
    ]
