# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-15 22:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courses',
            old_name='descriptiom',
            new_name='description',
        ),
    ]
