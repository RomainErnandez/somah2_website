# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-23 13:28
from __future__ import unicode_literals

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, default='unknown', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, default='unknown', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='company',
            field=models.CharField(blank=True, default='unknown', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2),
        ),
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='postal_code',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
