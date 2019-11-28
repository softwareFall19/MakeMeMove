# Generated by Django 2.2.7 on 2019-11-24 02:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0009_auto_20191118_0528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='home',
            name='is_posted',
            field=models.BooleanField(default=True),
        ),
    ]