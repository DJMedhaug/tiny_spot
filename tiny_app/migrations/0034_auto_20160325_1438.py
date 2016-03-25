# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiny_app', '0033_auto_20160325_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='file',
            field=models.ImageField(upload_to='/Users/danamedhaug/Documents/ProjectsFolder/static_in_env/static_root'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pic',
            field=models.ImageField(upload_to='/Users/danamedhaug/Documents/ProjectsFolder/static_in_env/static_root', blank=True),
        ),
    ]
