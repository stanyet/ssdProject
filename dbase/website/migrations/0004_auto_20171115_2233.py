# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-16 04:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20171115_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, upload_to='users/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='profile',
            name='profileFilled',
            field=models.IntegerField(default=0),
        ),
    ]