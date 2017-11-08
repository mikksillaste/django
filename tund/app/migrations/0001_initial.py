# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-08 12:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tuba',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toa_number', models.IntegerField(default=1)),
                ('kylalise_nimi', models.CharField(max_length=200)),
                ('valjumise_kuupaev', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
