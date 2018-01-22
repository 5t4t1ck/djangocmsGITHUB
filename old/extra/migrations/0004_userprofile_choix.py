# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extra', '0003_auto_20170605_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='choix',
            field=models.IntegerField(default=1, choices=[(1, 'Not relevant'), (2, 'Review'), (3, 'Maybe relevant'), (4, 'Relevant'), (5, 'Leading candidate')]),
        ),
    ]
