# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-03 14:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0004_auto_20190603_1312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='residence',
            name='neighbourhood',
        ),
        migrations.RemoveField(
            model_name='residence',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='Residence',
        ),
    ]
