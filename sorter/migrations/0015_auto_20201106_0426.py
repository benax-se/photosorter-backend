# Generated by Django 3.1.2 on 2020-11-06 01:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sorter', '0014_auto_20201106_0426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagenode',
            name='relatet',
        ),
        migrations.AddField(
            model_name='imagenode',
            name='relateto',
            field=models.ManyToManyField(related_name='_imagenode_relateto_+', to='sorter.ImageNode', verbose_name='Связан с'),
        ),
        migrations.AlterField(
            model_name='errorlog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 6, 4, 26, 53, 181787)),
        ),
    ]
