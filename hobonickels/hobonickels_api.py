#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import urllib
from hobonickels_utils import exchange
from hobonickels_utils import blockexplorer

__title__   = 'hobonickels'
__version__ = '0.1'
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


def to_btc():
	"""Returns array with trading pair object."""
	
	d = urllib.urlopen(exchange('hbn_btc'))
	return json.loads(d.read())
