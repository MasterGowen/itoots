# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ITOOTS.ticket.models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0003_auto_20151018_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='file',
            field=models.FileField(upload_to=ITOOTS.ticket.models.generate_new_filename),
        ),
    ]
