# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('extra', '0006_auto_20170608_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='creation',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2017, 6, 12, 19, 48, 20, 628789, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
