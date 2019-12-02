# Generated by Django 2.2.7 on 2019-12-02 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=150)),
                ('home_id', models.IntegerField()),
                ('info', models.TextField()),
                ('user_id', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactRental',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=150)),
                ('rental_id', models.IntegerField()),
                ('information', models.TextField()),
                ('user_id', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
