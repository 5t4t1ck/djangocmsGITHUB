# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extra', '0013_pessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messagerie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(blank=True, default='')),
                ('sender', models.CharField(blank=True, max_length=20, default='')),
                ('receiver', models.CharField(blank=True, max_length=20, default='')),
                ('read', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
