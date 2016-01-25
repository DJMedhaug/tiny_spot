# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiny_app', '0010_picture'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Picture',
        ),
    ]
