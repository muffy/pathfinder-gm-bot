# Generated by Django 2.0.5 on 2018-05-12 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gm', '0003_auto_20180512_0408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='encountercharacters',
            name='player',
        ),
        migrations.RemoveField(
            model_name='encountercharacters',
            name='start_round',
        ),
        migrations.AddField(
            model_name='encounter',
            name='start_round',
            field=models.IntegerField(default=0),
        ),
    ]
