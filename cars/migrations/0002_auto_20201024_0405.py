# Generated by Django 3.1.2 on 2020-10-24 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='door',
            field=models.PositiveIntegerField(max_length=1),
        ),
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.PositiveIntegerField(max_length=4),
        ),
    ]