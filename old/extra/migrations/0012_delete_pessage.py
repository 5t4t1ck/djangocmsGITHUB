# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extra', '0011_pessage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pessage',
        ),
    ]
