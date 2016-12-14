# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-14 08:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('downloads', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Mirror',
        ),
        migrations.AlterField(
            model_name='download',
            name='platform',
            field=models.CharField(choices=[(b'source', 'Source code'), (b'win32', 'Windows binaries')], max_length=100),
        ),
    ]
