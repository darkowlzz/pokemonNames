#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pokemoNames
----------------------------------

Tests for `pokemonNames` module.
"""

import unittest
import os

from pokemonNames.pokemonNames import PokemonNames

this_dir, this_file = os.path.split(__file__)
DATA_PATH = os.path.join(this_dir, 'foo.list')


class TestPokemonNames(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_random_name(self):
        p = PokemonNames()
        name = p.get_random_name()
        assert type(name) is str

    def test_get_name(self):
        p = PokemonNames()
        assert p.get_name(1) == 'Bulbasaur'
        assert p.get_name(25) == 'Pikachu'
        assert p.get_name(719) == 'Diancie'

    def test_get_from_indexedFile(self):
        p = PokemonNames(False)
        newDict = p.get_from_indexedFile(DATA_PATH)
        assert len(newDict) is 4
        assert newDict[14] == 'pinkpanda'

    def test_append_to_list(self):
        p = PokemonNames()
        assert p.get_name(1) == 'Bulbasaur'
        p.append_to_list(['firefox', 'waterfox'], start=900)
        assert p.get_name(900) == 'firefox'
        assert p.get_name(901) == 'waterfox'
        p.append_to_list(['airfox'], start=1)
        assert p.get_name(1) == 'airfox'
        p.append_to_list(DATA_PATH, hasIndex=True)
        assert p.get_name(14) == 'pinkpanda'

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
