# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 08:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cag_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='NewsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_title', models.CharField(max_length=50)),
                ('news_content', models.TextField(max_length=5000)),
                ('news_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.NewsCategory')),
            ],
        ),
    ]
