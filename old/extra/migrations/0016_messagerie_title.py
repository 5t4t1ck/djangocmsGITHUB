# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extra', '0015_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagerie',
            name='title',
            field=models.CharField(default='', max_length=200, blank=True),
        ),
    ]
