#!/usr/bin/env python
# -*- coding: utf-8 -*-

HBN_BLOCKEXPLORER = 'http://hbn.blockx.info/get/chain/HoboNickels/q/'
CRYPTOCOIN_API = 'http://www.cryptocoincharts.info/v2/api/tradingPair/'

def blockexplorer(*suffix):
	"""Returns the entrypoint URL for the Hobonickels block API.
	   All data provided by hbn.blockx.info.
	   http://www.worldcoinexplorer.com
	"""
	
	return HBN_BLOCKEXPLORER + '/'.join(suffix)

def exchange(*suffix):
	"""Returns the entrypoint URL for the Worldcoin price API.
	   All data provided by CryptoCoin.
	   http://www.cryptocoincharts.info
	"""
	
	return CRYPTOCOIN_API + '/'.join(suffix)
