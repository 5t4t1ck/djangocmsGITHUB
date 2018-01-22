# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extra', '0005_auto_20170607_1244'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authorization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('stage1', models.BooleanField(default=False)),
                ('stage2', models.BooleanField(default=False)),
                ('stage3', models.BooleanField(default=False)),
                ('user', models.ForeignKey(to='extra.UserProfile')),
            ],
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='q1',
            field=models.IntegerField(verbose_name='q1', blank=True, choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=0),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='q21',
            field=models.BooleanField(verbose_name='q21', choices=[(True, 'True'), (False, 'False')], default=False),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='q22',
            field=models.BooleanField(verbose_name='q22', choices=[(True, 'True'), (False, 'False')], default=False),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='q23',
            field=models.BooleanField(verbose_name='q23', choices=[(True, 'True'), (False, 'False')], default=False),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='q31',
            field=models.BooleanField(verbose_name='q31', choices=[(True, 'True'), (False, 'False')], default=False),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='q32',
            field=models.BooleanField(verbose_name='q32', choices=[(True, 'True'), (False, 'False')], default=False),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='q33',
            field=models.BooleanField(verbose_name='q33', choices=[(True, 'True'), (False, 'False')], default=False),
        ),
    ]
