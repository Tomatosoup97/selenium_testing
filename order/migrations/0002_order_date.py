# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-12 19:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 12, 19, 31, 32, 369499, tzinfo=utc)),
            preserve_default=False,
        ),
    ]