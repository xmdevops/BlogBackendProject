# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-09 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20171208_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articleinfo',
            name='front_image_type',
            field=models.CharField(choices=[('0', '无'), ('1', '小图'), ('2', '大图')], default='0', help_text='封面图类别', max_length=20, verbose_name='封面图类别'),
        ),
    ]