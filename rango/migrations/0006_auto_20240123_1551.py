# Generated by Django 2.2.28 on 2024-01-23 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0005_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
