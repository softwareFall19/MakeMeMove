# Generated by Django 2.2.7 on 2019-12-01 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_auto_20191201_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='address',
            field=models.CharField(default='', max_length=150),
        ),
    ]
