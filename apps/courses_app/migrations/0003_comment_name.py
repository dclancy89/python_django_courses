# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-08 01:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default='Anonymous', max_length=50),
            preserve_default=False,
        ),
    ]