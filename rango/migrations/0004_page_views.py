# Generated by Django 2.2.28 on 2024-01-23 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0003_auto_20240123_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
