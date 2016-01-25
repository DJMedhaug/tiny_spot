# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('tiny_app', '0011_delete_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('uploaded_file', models.FileField(max_length=255, upload_to='temp_uploads', storage=django.core.files.storage.FileSystemStorage(location='/Users/danamedhaug/Documents/ProjectsFolder/static_in_env/media_root'))),
                ('original_filename', models.CharField(max_length=255)),
                ('field_name', models.CharField(max_length=255, blank=True, null=True)),
                ('file_id', models.CharField(max_length=40)),
                ('form_id', models.CharField(max_length=40)),
            ],
        ),
    ]
