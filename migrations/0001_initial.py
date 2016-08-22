# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('pokedex', models.IntegerField(primary_key=True, serialize=False)),
                ('name_en', models.CharField(max_length=255)),
                ('name_de', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Spawn',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('pokemon', models.ForeignKey(to='pokedb.Pokemon')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Spawnpoint',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='spawn',
            name='spawnpoint',
            field=models.ForeignKey(to='pokedb.Spawnpoint'),
            preserve_default=True,
        ),
    ]
