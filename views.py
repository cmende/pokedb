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

import csv
from datetime import datetime
from io import StringIO

from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render

from .forms import ImportForm
from .models import Pokemon, Spawnpoint, Spawn

def index(request, pokedex=None, spawnpoint=None):
    sort = request.GET.get('sort', 'timestamp')
    if sort is 'timestamp' or sort not in ['pokemon', 'spawnpoint']:
        sort = '-timestamp'
    if pokedex is not None:
        spawns = Spawn.objects.filter(pokemon__pokedex=pokedex)
    elif spawnpoint is not None:
        spawns = Spawn.objects.filter(spawnpoint__id=spawnpoint)
    else:
        spawns = Spawn.objects.all()
    spawns = spawns.order_by(sort)
    return render(request, 'pokedb/index.html', {'spawns': spawns, 'sort': sort})

@permission_required('pokedb.add_spawn')
def import_spawns(request):
    form = ImportForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        handle_spawns_upload(request.FILES['file'])
    return render(request, 'pokedb/import_spawns.html', {'form': form})

@transaction.atomic
def handle_spawns_upload(f):
    csvf = StringIO(f.read().decode())
    reader = csv.reader(csvf)
    for row in reader:
        timestamp, pokemon_name, latitude, longitude = row

        # convert timestamp
        timestamp_dt = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')

        # fetch pokemon
        pokemon = Pokemon.objects.get(name_en=pokemon_name)

        # fetch spawnpoint
        spawnpoint = Spawnpoint.objects.get_or_create(latitude=latitude,
                longitude=longitude)[0]

        # save spawn
        Spawn.objects.update_or_create(timestamp=timestamp_dt,
                spawnpoint=spawnpoint, pokemon=pokemon)


@permission_required('pokedb.add_pokemon')
def import_pokemons(request):
    form = ImportForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        handle_pokemons_upload(request.FILES['file'])
    return render(request, 'pokedb/import_pokemons.html', {'form': form})

@transaction.atomic
def handle_pokemons_upload(f):
    csvf = StringIO(f.read().decode())
    dr = csv.DictReader(csvf)
    for row in dr:
        Pokemon.objects.update_or_create(pokedex=row['pkmnid'],
                defaults={'name_en': row['pkmnnameen'],
                    'name_de': row['pkmnnamede']})
