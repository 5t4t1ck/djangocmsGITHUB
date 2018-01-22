# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kine', '0002_auto_20170605_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='kineprofile',
            name='photos',
            field=models.ImageField(null=True, blank=True, upload_to='/djangocms/media/', verbose_name='Profile Picture'),
        ),
    ]
