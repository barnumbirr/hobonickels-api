#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import urllib
from hobonickels_utils import get_addr
from hobonickels_utils import exchange
from hobonickels_utils import gen_eckey
from hobonickels_utils import blockexplorer

__title__   = 'hobonickels'
__version__ = '1.0.1'
__author__  = '@c0ding'
__repo__    = 'https://github.com/c0ding/hobonickels-api'
__license__ = 'Apache v2.0 License'


def about():
	"""Returns some information about the hobonickels module."""

	return '{} v.{} is maintained by {} and available at {}.'.format(__title__, __version__, __author__, __repo__)


def difficulty():
	"""Returns the current network difficulty."""

	d = urllib.urlopen(blockexplorer('getdifficulty'))
	return float(d.read())


def hashrate():
	"""Returns the current network hashrate."""

	c = block_count()
	blocks = "%.0f" %c
	d = urllib.urlopen(blockexplorer('nethash') + '/' + str(blocks))
	last_line = d.readlines()[-1]
	e = last_line.split(',')
	return e[-1]


def block_count():
	"""Returns the number of blocks in the longest block chain.
	   Equivalent to Bitcoin's getblockcount.
	"""

	d = urllib.urlopen(blockexplorer('getblockcount'))
	return float(d.read())


def total_coins():
	"""Returns the number of Hobonickels mined."""
	
	d = urllib.urlopen(blockexplorer('totalbc'))
	return float(d.read())


def addressbalance(PARAMETER):
	"""Returns the address balance.
	   [PARAMETER] is required and should be a HBN address.
	"""
	
	d = urllib.urlopen(blockexplorer('addressbalance') + '/' + str(PARAMETER))
	return float(d.read())


def addresstohash(PARAMETER):
	"""Returns the public key hash encoded in an address.
	   [PARAMETER] is required and should be a HBN address.
	"""
	
	d = urllib.urlopen(blockexplorer('addresstohash') + '/' + str(PARAMETER))
	return d.read()


def checkaddress(PARAMETER):
	"""Checks if specified address is valid and returns
	   _pubkeyhash_version_byte.
	   [PARAMETER] is required and can be any crypto address.
	"""

	d = urllib.urlopen(blockexplorer('checkaddress') + '/' + str(PARAMETER))
	return d.read()


def decode_address(PARAMETER):
	 """Returns the version prefix and hash encoded in an address
	    [PARAMETER] is required and can be any crypto address.
	 """

	 d = urllib.urlopen(blockexplorer('decode_address') + '/' + str(PARAMETER))
	 return d.read()


def getreceivedbyaddress(PARAMETER):
	"""Returns amount of HBN received by an address.
	   [PARAMETER] is required and should be a HBN address.
	"""

	d = urllib.urlopen(blockexplorer('getreceivedbyaddress') + '/' + str(PARAMETER))
	return d.read()


def getsentbyaddress(PARAMETER):
	"""Returns amount of HBN sent by an address.
	   [PARAMETER] is required and should be a HBN address.
	"""

	d = urllib.urlopen(blockexplorer('getsentbyaddress') + '/' + str(PARAMETER))
	return d.read()


def hashpubkey(PARAMETER):
	"""Returns the 160-bit hash of PUBKEY.
	   [PARAMETER] is required and should be a PUBKEY.
	"""

	d = urllib.urlopen(blockexplorer('hashpubkey') + '/' + str(PARAMETER))
	return d.read()


def hashtoaddress(PARAMETER):
	"""Converts a 160-bit hash to an address.
	   [PARAMETER] is required and should be an address hash.
	"""

	d = urllib.urlopen(blockexplorer('hashtoaddress') + '/' + str(PARAMETER))
	return d.read()


def translate_address(PARAMETER):
	"""Translates address for use in HBN chain
	   [PARAMETER] is required and can be any crypto address.
	"""

	d = urllib.urlopen(blockexplorer('translate_address') + '/' + str(PARAMETER))
	return d.read()
	

def generate_address():
	"""Returns a valid Hobonickels address and it's
	   matching private key.
	   On OSX run this in i386 mode.
	"""

	return get_addr(gen_eckey(compressed=True,version=34),version=34)


def to_btc():
	"""Returns array with trading pair object."""
	
	d = urllib.urlopen(exchange('hbn_btc'))
	return json.loads(d.read())
