# Generated by Django 2.2.7 on 2019-11-18 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0005_auto_20191113_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='information',
            field=models.TextField(default=''),
        ),
    ]