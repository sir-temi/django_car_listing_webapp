# Generated by Django 3.1.2 on 2020-10-28 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0010_auto_20201025_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='model',
            field=models.CharField(default=11111, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='price',
            field=models.PositiveIntegerField(default=111111),
            preserve_default=False,
        ),
    ]
