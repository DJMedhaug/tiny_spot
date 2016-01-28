# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tiny_app', '0019_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 1, 28, 19, 52, 4, 917889, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
