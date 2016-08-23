# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokedb', '0002_auto_20160821_1534'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='spawn',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AddField(
            model_name='spawnpoint',
            name='name',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
    ]
