# Copyright 2016 Christoph Mende 
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.db import models

class Spawnpoint(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        unique_together = ('latitude', 'longitude',)

    def __str__(self):
        return "{}, {}".format(self.latitude, self.longitude)

class Pokemon(models.Model):
    pokedex = models.IntegerField(primary_key=True)
    name_en = models.CharField(max_length=255,unique=True)
    name_de = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.name_de

class Spawn(models.Model):
    timestamp = models.DateTimeField()
    spawnpoint = models.ForeignKey('Spawnpoint')
    pokemon = models.ForeignKey('Pokemon')

    def __str__(self):
        return "{} um {} bei {}".format(self.pokemon, self.timestamp,
                self.spawnpoint)

    class Meta:
        ordering = ['-timestamp']
