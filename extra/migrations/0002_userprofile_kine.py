# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extra', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='kine',
            field=models.CharField(default='', blank=True, max_length=20),
        ),
    ]
