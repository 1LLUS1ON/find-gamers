# Generated by Django 3.1.2 on 2021-01-19 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamers', '0011_auto_20210119_1644'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matchpt',
            name='game',
        ),
    ]