# Generated by Django 2.2.7 on 2019-11-24 16:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('renters', '0003_auto_20191124_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
