# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extra', '0014_messagerie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('userreceiver', models.CharField(max_length=20, default='', blank=True)),
                ('user', models.ForeignKey(to='extra.UserProfile')),
            ],
        ),
    ]
