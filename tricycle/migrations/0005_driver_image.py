# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-15 12:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tricycle', '0004_operator_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='image',
            field=models.FileField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]