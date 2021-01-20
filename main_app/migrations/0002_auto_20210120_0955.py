# Generated by Django 2.2.12 on 2021-01-20 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='city',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='city',
            name='image',
            field=models.URLField(default='', max_length=1000, verbose_name=''),
        ),
    ]
