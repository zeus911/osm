# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-09 03:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupname', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='groupname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.UserGroup'),
        ),
    ]
