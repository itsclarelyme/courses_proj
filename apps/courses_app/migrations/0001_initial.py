# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-15 22:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=45)),
                ('descriptiom', models.TextField(null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]