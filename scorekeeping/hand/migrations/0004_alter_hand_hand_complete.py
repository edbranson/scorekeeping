# Generated by Django 3.2.7 on 2021-10-22 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hand', '0003_playerhand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hand',
            name='hand_complete',
            field=models.BooleanField(),
        ),
    ]
