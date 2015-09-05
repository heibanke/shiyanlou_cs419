# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='\u7c7b\u522b\u540d\u79f0')),
                ('isIncome', models.BooleanField(verbose_name='\u662f\u5426\u6536\u5165', choices=[(True, '\u6536\u5165'), (False, '\u652f\u51fa')])),
                ('p_category', models.ForeignKey(related_name='childs', verbose_name='\u7236\u7c7b\u540d\u79f0', blank=True, to='jizhang.Category', null=True)),
                ('user', models.ForeignKey(verbose_name='\u6240\u5c5e\u7528\u6237', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.DecimalField(verbose_name='\u91d1\u989d', max_digits=20, decimal_places=2)),
                ('comment', models.CharField(max_length=200, verbose_name='\u6ce8\u91ca', blank=True)),
                ('pub_date', models.DateField(verbose_name='\u65e5\u671f')),
                ('category', models.ForeignKey(related_name='items', verbose_name='\u5206\u7c7b', to='jizhang.Category')),
            ],
        ),
    ]
