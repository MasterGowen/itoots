# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachment',
            name='filename',
            field=models.CharField(null=True, verbose_name='Filename:', max_length=255),
        ),
        migrations.AddField(
            model_name='ticket',
            name='author_email',
            field=models.EmailField(null=True, max_length=254),
        ),
        migrations.AddField(
            model_name='ticket',
            name='author_name',
            field=models.CharField(null=True, max_length=64),
        ),
        migrations.AddField(
            model_name='ticket',
            name='subject',
            field=models.CharField(null=True, max_length=1024),
        ),
        migrations.AddField(
            model_name='ticket',
            name='text',
            field=models.TextField(null=True, max_length=4096),
        ),
    ]
