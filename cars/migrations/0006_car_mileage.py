# Generated by Django 3.1.2 on 2020-10-25 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_car_slugy'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='mileage',
            field=models.PositiveIntegerField(default=78888),
            preserve_default=False,
        ),
    ]
