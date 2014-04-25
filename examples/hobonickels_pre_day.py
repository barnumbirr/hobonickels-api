#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hobonickels

def estimated_hbn(hashrate):
	"""Returns an estimated amount of Hobonickels a given
	   hashrate will yield at a given difficulty and reward.
	   This profit is NOT guaranteed.
	"""
	
	difficulty = hobonickels.difficulty()
	reward = 5
	estimated = float(hashrate) * float(1000) * float(86400) * float(reward) / (float(4294967296) * float(difficulty))
	estimated = '%.2f' % estimated
	print 'A hashrate of {} khash/s and a difficulty of {} will yield {}HBN per day.'.format(hashrate, difficulty, estimated)

if __name__ == '__main__':
	estimated_hbn(hashrate)
