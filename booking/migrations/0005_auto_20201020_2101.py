# Generated by Django 2.2 on 2020-10-21 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_auto_20201020_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='checkin',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='checkout',
            field=models.DateField(),
        ),
    ]
