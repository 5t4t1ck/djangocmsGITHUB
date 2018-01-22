# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extra', '0002_userprofile_kine'),
    ]

    operations = [
        migrations.CreateModel(
            name='KineToUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kine', models.CharField(max_length=10, blank=True, default='')),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='kine',
        ),
        migrations.AddField(
            model_name='kinetouser',
            name='user',
            field=models.ForeignKey(to='extra.UserProfile'),
        ),
    ]
