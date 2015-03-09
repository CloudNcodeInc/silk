# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=300, default='', blank=True)),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_time', models.DateTimeField(null=True, blank=True)),
                ('time_taken', models.FloatField(null=True, blank=True)),
                ('file_path', models.CharField(max_length=300, default='', blank=True)),
                ('line_num', models.IntegerField(null=True, blank=True)),
                ('end_line_num', models.IntegerField(null=True, blank=True)),
                ('func_name', models.CharField(max_length=300, default='', blank=True)),
                ('exception_raised', models.BooleanField(default=False)),
                ('dynamic', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('path', models.CharField(max_length=300, db_index=True)),
                ('query_params', models.TextField(default='', blank=True)),
                ('raw_body', models.TextField(default='', blank=True)),
                ('body', models.TextField(default='', blank=True)),
                ('method', models.CharField(max_length=10)),
                ('start_time', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('view_name', models.CharField(max_length=300, db_index=True, default='', blank=True)),
                ('end_time', models.DateTimeField(null=True, blank=True)),
                ('time_taken', models.FloatField(null=True, blank=True)),
                ('encoded_headers', models.TextField(default='', blank=True)),
                ('meta_time', models.FloatField(null=True, blank=True)),
                ('meta_num_queries', models.IntegerField(null=True, blank=True)),
                ('meta_time_spent_queries', models.FloatField(null=True, blank=True)),
                ('pyprofile', models.TextField(default='', blank=True)),
                ('num_sql_queries', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('status_code', models.IntegerField()),
                ('raw_body', models.TextField(default='', blank=True)),
                ('body', models.TextField(default='', blank=True)),
                ('encoded_headers', models.TextField(default='', blank=True)),
                ('request', models.OneToOneField(to='silk.Request', related_name='response')),
            ],
        ),
        migrations.CreateModel(
            name='SQLQuery',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('query', models.TextField()),
                ('start_time', models.DateTimeField(null=True, default=django.utils.timezone.now, blank=True)),
                ('end_time', models.DateTimeField(null=True, blank=True)),
                ('time_taken', models.FloatField(null=True, blank=True)),
                ('traceback', models.TextField()),
                ('request', models.ForeignKey(related_name='queries', to='silk.Request', null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='queries',
            field=models.ManyToManyField(db_index=True, to='silk.SQLQuery', related_name='profiles'),
        ),
        migrations.AddField(
            model_name='profile',
            name='request',
            field=models.ForeignKey(to='silk.Request', null=True, blank=True),
        ),
    ]
