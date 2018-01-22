# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('bio', models.TextField(default='', blank=True)),
                ('phone', models.CharField(default='', max_length=20, blank=True)),
                ('city', models.CharField(default='', max_length=100, blank=True)),
                ('country', models.CharField(default='', max_length=100, blank=True)),
                ('organization', models.CharField(default='', max_length=100, blank=True)),
                ('user', models.OneToOneField(related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
