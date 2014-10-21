# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phonedb.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('medium', models.CharField(max_length=100, choices=[(b'usb', b'USB'), (b'serial', b'Serial'), (b'irda', b'IrDA'), (b'bluetooth', b'Bluetooth'), (b'other', b'Other')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Phone name, please exclude vendor name.', max_length=250, validators=[phonedb.models.phone_name_validator])),
                ('model', models.CharField(help_text='Model used in Gammu configuration, usually empty.', max_length=100, blank=True)),
                ('gammu_version', models.CharField(help_text='Gammu version where you tested this phone.', max_length=100, blank=True)),
                ('note', models.TextField(help_text='Any note about this phone and Gammu support for it. You can use <a href="http://daringfireball.net/projects/markdown/syntax">markdown markup</a>.', blank=True)),
                ('note_html', models.TextField(editable=False, blank=True)),
                ('author_name', models.CharField(max_length=250, blank=True)),
                ('author_email', models.EmailField(help_text='Please choose how will be email handled in next field.', max_length=250, blank=True)),
                ('email_garble', models.CharField(default=b'atdot', max_length=100, choices=[(b'atdot', 'Use [at] and [dot]'), (b'none', 'Display it normally'), (b'hide', "Don't show email at all"), (b'nospam', 'Insert NOSPAM text at random position')])),
                ('state', models.CharField(default=b'draft', max_length=100, db_index=True, choices=[(b'draft', 'Draft'), (b'approved', 'Approved'), (b'deleted', 'Deleted')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('address', models.CharField(max_length=100, blank=True)),
                ('hostname', models.CharField(max_length=100, blank=True)),
                ('connection', models.ForeignKey(blank=True, to='phonedb.Connection', help_text='Connection used in Gammu configuration.', null=True)),
                ('features', models.ManyToManyField(help_text='Features which are working in Gammu.', to='phonedb.Feature', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('url', models.URLField(max_length=250)),
                ('slug', models.SlugField(unique=True)),
                ('tuxmobil', models.SlugField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='phone',
            name='vendor',
            field=models.ForeignKey(to='phonedb.Vendor'),
            preserve_default=True,
        ),
    ]
