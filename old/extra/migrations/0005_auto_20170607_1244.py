# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extra', '0004_userprofile_choix'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('q1', models.IntegerField(verbose_name='q1', choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9')], blank=True, default='')),
                ('q21', models.BooleanField(verbose_name='q21', choices=[(True, 'True'), (False, 'False')], default='')),
                ('q22', models.BooleanField(verbose_name='q22', choices=[(True, 'True'), (False, 'False')], default='')),
                ('q23', models.BooleanField(verbose_name='q23', choices=[(True, 'True'), (False, 'False')], default='')),
                ('q31', models.BooleanField(verbose_name='q31', choices=[(True, 'True'), (False, 'False')], default='')),
                ('q32', models.BooleanField(verbose_name='q32', choices=[(True, 'True'), (False, 'False')], default='')),
                ('q33', models.BooleanField(verbose_name='q33', choices=[(True, 'True'), (False, 'False')], default='')),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='choix',
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='user',
            field=models.ForeignKey(to='extra.UserProfile'),
        ),
    ]
