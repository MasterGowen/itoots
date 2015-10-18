# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0002_auto_20151017_2225'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachment',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='id',
            field=models.CharField(serialize=False, default='None', max_length=32, primary_key=True),
        ),
    ]
