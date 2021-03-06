# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-24 18:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_ik_miniature'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=10000)),
                ('auteur', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date de parution')),
                ('fichier', models.FileField(default=None, upload_to='uploads/articles/')),
            ],
        ),
    ]
