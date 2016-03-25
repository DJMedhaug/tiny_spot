# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiny_app', '0025_auto_20160317_1455'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='photo',
        ),
        migrations.AddField(
            model_name='post',
            name='pic',
            field=models.ImageField(blank=True, upload_to='/Users/danamedhaug/Documents/ProjectsFolder/static_in_env/media_root'),
        ),
    ]
