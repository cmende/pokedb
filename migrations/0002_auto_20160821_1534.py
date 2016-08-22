# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokedb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='name_de',
            field=models.CharField(unique=True, max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='name_en',
            field=models.CharField(unique=True, max_length=255),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='spawnpoint',
            unique_together=set([('latitude', 'longitude')]),
        ),
    ]
