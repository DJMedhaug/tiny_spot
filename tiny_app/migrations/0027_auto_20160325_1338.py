# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiny_app', '0026_auto_20160317_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='file',
            field=models.ImageField(upload_to='/static/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pic',
            field=models.ImageField(blank=True, upload_to='/static/'),
        ),
    ]
