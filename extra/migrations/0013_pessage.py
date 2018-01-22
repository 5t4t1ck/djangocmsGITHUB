# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extra', '0012_delete_pessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessage',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('user_names', models.CharField(max_length=20)),
                ('pessage', models.CharField(max_length=140)),
                ('user', models.ForeignKey(to='extra.UserProfile')),
            ],
        ),
    ]
