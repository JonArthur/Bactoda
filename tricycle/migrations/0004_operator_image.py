# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-15 07:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tricycle', '0003_auto_20170815_0404'),
    ]

    operations = [
        migrations.AddField(
            model_name='operator',
            name='image',
            field=models.FileField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]
