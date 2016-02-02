# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiny_app', '0022_auto_20160201_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='file',
            field=models.ImageField(upload_to='/Users/danamedhaug/Documents/ProjectsFolder/static_in_env/media_root'),
        ),
    ]
