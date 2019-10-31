# Generated by Django 2.2.6 on 2019-10-29 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('picture', models.ImageField(upload_to='pictures/%Y/%m/%d/')),
                ('information', models.TextField(blank=True)),
                ('telephone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=40)),
            ],
        ),
    ]
