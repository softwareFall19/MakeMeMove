# Generated by Django 2.2.7 on 2019-12-01 23:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_contact_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='address',
        ),
    ]