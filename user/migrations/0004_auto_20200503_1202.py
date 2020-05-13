# Generated by Django 3.0.2 on 2020-05-03 12:02

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20200503_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='biodatamodel',
            name='age',
            field=models.IntegerField(default=22),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usermoreinfomodel',
            name='hobby',
            field=user.models.ListField(max_length=100),
        ),
        migrations.AlterField(
            model_name='usermoreinfomodel',
            name='music',
            field=user.models.ListField(max_length=100),
        ),
        migrations.AlterField(
            model_name='usermoreinfomodel',
            name='sport',
            field=user.models.ListField(max_length=100),
        ),
    ]
