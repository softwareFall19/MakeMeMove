# Generated by Django 2.2.7 on 2019-11-13 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='userID',
            new_name='user_id',
        ),
    ]
