# Generated by Django 2.2.12 on 2021-01-20 20:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20210120_0955'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]