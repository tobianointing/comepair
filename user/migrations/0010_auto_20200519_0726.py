# Generated by Django 3.0.2 on 2020-05-19 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20200519_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermoreinfomodel',
            name='do_you_smoke',
            field=models.CharField(choices=[('Never', 'Never'), ('On special occasion', 'On special occasion'), ('Once a week', 'Once a week'), ('Few times a week', 'Few times a week'), ('Daily', 'Daily')], default='Non-smoker', max_length=500),
        ),
        migrations.AlterField(
            model_name='usermoreinfomodel',
            name='do_you_take_alcohol',
            field=models.CharField(choices=[('Non-smoker', 'Non-smoker'), ('Occasional smoker', 'Occasional smoker'), ('Smoker', 'Smoker')], default='Never', max_length=500),
        ),
    ]