# Generated by Django 2.0.5 on 2018-05-18 01:41

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('game', '0005_auto_20180515_0109'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='player',
            options={},
        ),
        migrations.RemoveField(
            model_name='player',
            name='name',
        ),
        migrations.AddField(
            model_name='character',
            name='nicknames',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), default=[], size=None),
        ),
        migrations.AddField(
            model_name='player',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
