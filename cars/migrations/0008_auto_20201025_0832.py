# Generated by Django 3.1.2 on 2020-10-25 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_auto_20201025_0347'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='door',
            new_name='doors',
        ),
        migrations.RemoveField(
            model_name='car',
            name='description',
        ),
        migrations.AddField(
            model_name='car',
            name='mainpic',
            field=models.ImageField(default='dfhfhf', upload_to='images'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='pic1',
            field=models.ImageField(default='djjjfj', upload_to='images'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='pic2',
            field=models.ImageField(default='dkfkfk', upload_to='images'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='pic3',
            field=models.ImageField(default='fff', upload_to='images'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='pic4',
            field=models.ImageField(default='djfjfjf', upload_to='images'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='pic5',
            field=models.ImageField(default='kdjjfj', upload_to='images'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='car',
            name='transmission',
            field=models.CharField(choices=[(None, 'Choose'), ('Automatic', 'Automatic'), ('Manual', 'Manual')], max_length=10),
        ),
    ]
