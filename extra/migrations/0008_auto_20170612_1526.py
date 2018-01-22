# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extra', '0007_questionnaire_creation'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayStage1',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now=True)),
                ('day', models.IntegerField(default=0, blank=True)),
                ('ex1set1', models.BooleanField(default=False)),
                ('ex1set2', models.BooleanField(default=False)),
                ('ex1set3', models.BooleanField(default=False)),
                ('ex2set1', models.BooleanField(default=False)),
                ('ex2set2', models.BooleanField(default=False)),
                ('ex2set3', models.BooleanField(default=False)),
                ('ex3set1', models.BooleanField(default=False)),
                ('ex3set2', models.BooleanField(default=False)),
                ('ex3set3', models.BooleanField(default=False)),
                ('ex4set1', models.BooleanField(default=False)),
                ('ex4set2', models.BooleanField(default=False)),
                ('ex4set3', models.BooleanField(default=False)),
                ('ex5set1', models.BooleanField(default=False)),
                ('ex5set2', models.BooleanField(default=False)),
                ('ex5set3', models.BooleanField(default=False)),
                ('ex6set1', models.BooleanField(default=False)),
                ('ex6set2', models.BooleanField(default=False)),
                ('ex6set3', models.BooleanField(default=False)),
                ('ex7set1', models.BooleanField(default=False)),
                ('ex7set2', models.BooleanField(default=False)),
                ('ex7set3', models.BooleanField(default=False)),
                ('ex8set1', models.BooleanField(default=False)),
                ('ex8set2', models.BooleanField(default=False)),
                ('ex8set3', models.BooleanField(default=False)),
                ('ex9set1', models.BooleanField(default=False)),
                ('ex9set2', models.BooleanField(default=False)),
                ('ex9set3', models.BooleanField(default=False)),
                ('cryo', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Stage1',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('begin', models.DateField(default='')),
                ('user', models.ForeignKey(to='extra.UserProfile')),
            ],
        ),
        migrations.AddField(
            model_name='daystage1',
            name='stage',
            field=models.ForeignKey(to='extra.Stage1'),
        ),
    ]
