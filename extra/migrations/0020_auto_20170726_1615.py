# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extra', '0019_auto_20170725_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(null=True, blank=True, upload_to='/djangocms/media/', verbose_name='Profile Picture'),
        ),
    ]
