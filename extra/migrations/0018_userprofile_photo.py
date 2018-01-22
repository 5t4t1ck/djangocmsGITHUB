# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extra', '0017_auto_20170712_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(verbose_name='Profile Picture', max_length=255, blank=True, upload_to='/media/', null=True),
        ),
    ]
