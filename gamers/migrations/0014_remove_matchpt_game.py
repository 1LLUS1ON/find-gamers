# Generated by Django 3.1.2 on 2021-01-19 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamers', '0013_matchpt_game'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matchpt',
            name='game',
        ),
    ]
