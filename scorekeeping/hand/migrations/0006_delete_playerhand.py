# Generated by Django 3.2.7 on 2021-10-22 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hand', '0005_alter_hand_hand_complete'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PlayerHand',
        ),
    ]