# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-10 16:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20160810_0240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='teachers',
            field=models.ManyToManyField(blank=True, related_name='students', to='students.Teacher'),
        ),
    ]