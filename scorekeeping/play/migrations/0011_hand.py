# Generated by Django 3.2.7 on 2021-10-22 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0010_delete_hand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hand_num', models.IntegerField()),
                ('hand_complete', models.BooleanField(null=True)),
                ('play', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='play.play')),
            ],
        ),
    ]