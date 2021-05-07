# Generated by Django 3.1.2 on 2020-10-29 21:04

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0013_auto_20201029_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='mainpic',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, quality=75, size=[600, 250], upload_to='images'),
        ),
    ]
