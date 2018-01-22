# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extra', '0016_messagerie_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagerie',
            name='delrec',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='messagerie',
            name='delsen',
            field=models.BooleanField(default=False),
        ),
    ]
