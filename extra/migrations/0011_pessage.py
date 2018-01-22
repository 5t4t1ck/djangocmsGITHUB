# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extra', '0010_auto_20170707_1155'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessage',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('user_names', models.CharField(max_length=20)),
                ('pessage', models.CharField(max_length=140)),
            ],
        ),
    ]
