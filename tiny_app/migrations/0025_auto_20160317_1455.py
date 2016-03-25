# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiny_app', '0024_auto_20160201_1039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='pic',
        ),
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(upload_to='photo', blank=True),
        ),
    ]
