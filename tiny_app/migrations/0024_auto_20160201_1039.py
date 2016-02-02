# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiny_app', '0023_auto_20160201_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pic',
            field=models.ImageField(upload_to='/Users/danamedhaug/Documents/ProjectsFolder/static_in_env/media_root', blank=True),
        ),
    ]
