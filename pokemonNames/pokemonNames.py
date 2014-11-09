#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from random import randrange


class PokemonNames():

    def __init__(self):
        '''Opens the name list and stores the names in a dictionary'''
        fd = open('pokemonNames/names.list', 'r+')
        lines = fd.readlines()
        self.totalCount = len(lines) + 1
        for i, val in enumerate(lines):
            lines[i] = val.split()
        self.nameDict = {}
        for line in lines:
            self.nameDict[int(line[0])] = line[1]

    def get_random_name(self):
        '''Return a random name'''
        key = randrange(1, self.totalCount)
        return self.nameDict[key]

    def get_name(self, key):
        '''Return a name for the given key
        Argument:
        key -- Pokemon number id (int)
        '''
        return self.nameDict[key]
