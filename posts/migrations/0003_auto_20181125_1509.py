# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-25 11:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20181124_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 25, 11, 9, 21, 248455, tzinfo=utc)),
        ),
    ]
