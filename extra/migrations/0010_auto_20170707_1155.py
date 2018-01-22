# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extra', '0009_auto_20170613_1141'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayStage2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('date', models.DateField(auto_now=True)),
                ('day', models.IntegerField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Stage2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('begin', models.DateField(default='2000-01-01')),
                ('user', models.ForeignKey(to='extra.UserProfile')),
            ],
        ),
        migrations.AddField(
            model_name='daystage2',
            name='stage',
            field=models.ForeignKey(to='extra.Stage2'),
        ),
    ]
