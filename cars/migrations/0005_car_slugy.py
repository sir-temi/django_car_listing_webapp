# Generated by Django 3.1.2 on 2020-10-25 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_auto_20201024_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='slugy',
            field=models.SlugField(allow_unicode=True, default='hi', unique=True),
            preserve_default=False,
        ),
    ]