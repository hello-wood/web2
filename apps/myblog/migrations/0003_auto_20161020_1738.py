# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-20 17:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_auto_20161020_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='bloginfo',
            name='cover_img',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='bloginfo',
            name='file_path',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='bloginfo',
            name='title',
            field=models.CharField(default='', max_length=255),
        ),
    ]
