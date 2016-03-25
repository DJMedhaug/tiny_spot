# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiny_app', '0035_auto_20160325_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='file',
            field=models.ImageField(upload_to='Users/danamedhaug/Documents/ProjectsFolder/static_in_env/media_root'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pic',
            field=models.ImageField(blank=True, upload_to='Users/danamedhaug/Documents/ProjectsFolder/static_in_env/media_root'),
        ),
    ]
