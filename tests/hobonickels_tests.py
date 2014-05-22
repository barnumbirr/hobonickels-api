#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.insert(0, os.path.abspath('..'))
import unittest
import hobonickels

__title__   = 'hobonickels'
__version__ = '1.0.1'
__author__  = '@c0ding'
__repo__    = 'https://github.com/c0ding/hobonickels-api'
__license__ = 'Apache v2.0 License'

class hobonickelstestsuite(unittest.TestCase):

	_multiprocess_can_split_ = True

	def test_difficulty(self):
		hobonickels.difficulty()
		assert type(hobonickels.difficulty()) is float
	
	def test_hashrate(self):
		hobonickels.hashrate()
		assert type(hobonickels.hashrate()) is str

	def test_block_count(self):
		hobonickels.block_count()
		assert type(hobonickels.block_count()) is float

	def test_total_coins(self):
		hobonickels.total_coins()
		assert type(hobonickels.total_coins()) is float
		
	def test_addressbalance(self):
		hobonickels.addressbalance('Es8mAQxXCKHA7YPnBhy4SzhLrmCH27sRu6')
		assert type(hobonickels.addressbalance('Es8mAQxXCKHA7YPnBhy4SzhLrmCH27sRu6')) is float
		
	def test_addresstohash(self):
		hobonickels.addresstohash('Es8mAQxXCKHA7YPnBhy4SzhLrmCH27sRu6')
		assert type(hobonickels.addresstohash('Es8mAQxXCKHA7YPnBhy4SzhLrmCH27sRu6')) is str
		
	def test_checkaddress(self):
		hobonickels.checkaddress('Es8mAQxXCKHA7YPnBhy4SzhLrmCH27sRu6')
		assert type(hobonickels.checkaddress('Es8mAQxXCKHA7YPnBhy4SzhLrmCH27sRu6')) is str
		
	def test_getreceivedbyaddress(self):
		hobonickels.getreceivedbyaddress('Es8mAQxXCKHA7YPnBhy4SzhLrmCH27sRu6')
		assert type(hobonickels.getreceivedbyaddress('Es8mAQxXCKHA7YPnBhy4SzhLrmCH27sRu6')) is str
		
	def test_getsentbyaddress(self):
		hobonickels.getsentbyaddress('Es8mAQxXCKHA7YPnBhy4SzhLrmCH27sRu6')
		assert type(hobonickels.getsentbyaddress('Es8mAQxXCKHA7YPnBhy4SzhLrmCH27sRu6')) is str
		
	def test_hashpubkey(self):
		hobonickels.hashpubkey('74BCE81E8F8FAAD31F32882132D3366CAA65EE46')
		assert type(hobonickels.hashpubkey('74BCE81E8F8FAAD31F32882132D3366CAA65EE46')) is str
		
	def test_hashtoaddress(self):
		hobonickels.hashtoaddress('74BCE81E8F8FAAD31F32882132D3366CAA65EE46')
		assert type(hobonickels.hashtoaddress('74BCE81E8F8FAAD31F32882132D3366CAA65EE46')) is str
		
	def test_translate_address(self):
		hobonickels.translate_address('Es8mAQxXCKHA7YPnBhy4SzhLrmCH27sRu6')
		assert type(hobonickels.translate_address('Es8mAQxXCKHA7YPnBhy4SzhLrmCH27sRu6')) is str
		
	def test_generate_address(self):
		hobonickels.generate_address()
		assert type(hobonickels.generate_address()) is str
		
	def test_to_btc(self):
		hobonickels.to_btc()
		assert type(hobonickels.to_btc()) is dict

if __name__ == '__main__':
    unittest.main()
