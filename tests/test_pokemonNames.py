#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pokemoNames
----------------------------------

Tests for `pokemonNames` module.
"""

import unittest

from pokemonNames.pokemonNames import PokemonNames


class TestPokemonNames(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_random_name(self):
        p = PokemonNames()
        name = p.get_random_name()
        assert type(name) is str

    def test_get_name(self):
        p = PokemonNames()
        name = p.get_name(1)
        assert name == 'Bulbasaur'
        name = p.get_name(25)
        assert name == 'Pikachu'
        name = p.get_name(719)
        assert name == 'Diancie'

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
