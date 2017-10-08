# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-07 17:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to=b'')),
                ('description', models.TextField(blank=True, default='', null=True)),
            ],
            options={
                'verbose_name': 'Grupo/Adherente',
                'verbose_name_plural': 'Grupos/Adherentes',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('image', models.ImageField(upload_to=b'')),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dataleufu.UserGroup')),
            ],
            options={
                'verbose_name': 'perfil',
                'verbose_name_plural': 'perfiles',
            },
        ),
    ]