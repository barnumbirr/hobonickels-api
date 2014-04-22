#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.insert(0, os.path.abspath('..'))
import unittest
import hobonickels

__title__   = 'hobonickels'
__version__ = '0.2'
__author__  = '@c0ding'
__repo__    = 'https://github.com/c0ding/hobonickels-api'
__license__ = 'Apache v2.0 License'

class hobonickelstestsuite(unittest.TestCase):

	_multiprocess_can_split_ = True

	def test_difficulty(self):
		hobonickels.difficulty()
		assert type(hobonickels.difficulty()) is float

	def test_block_count(self):
		hobonickels.block_count()
		assert type(hobonickels.block_count()) is float

	def test_total_coins(self):
		hobonickels.total_coins()
		assert type(hobonickels.total_coins()) is float
		
	def test_to_btc(self):
		hobonickels.to_btc()
		assert type(hobonickels.to_btc()) is dict

if __name__ == '__main__':
    unittest.main()
