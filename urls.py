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

from django.conf.urls import patterns, url, include

from . import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^pokemon/(?P<pokedex>\d+)$', views.index, name='pokemon'),
    url(r'^spawnpoint/(?P<spawnpoint>\d+)$', views.index, name='spawnpoint'),
    url(r'^import_spawns$', views.import_spawns, name='import_spawns'),
    url(r'^import_pokemons$', views.import_pokemons, name='import_pokemons'),
    url('', include('django.contrib.auth.urls')),
)
