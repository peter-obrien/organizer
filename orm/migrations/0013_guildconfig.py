# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-20 03:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0012_auto_20170916_1520'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuildConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guild', models.BigIntegerField()),
                ('alarm_source', models.BigIntegerField()),
                ('rsvp_channel', models.BigIntegerField()),
                ('command', models.CharField(max_length=1)),
            ],
        ),
    ]
