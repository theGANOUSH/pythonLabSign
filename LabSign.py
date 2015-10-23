#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py
#  
#  Copyright 2015  <pi@raspberrypi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
# 

import serial
import time
from threading import Thread


wordList = []

df = open("Dictionary.txt", "r+")

def inputThread(L):
	raw_input()
	L.append(None)

def getTime(x):
	y = (float(x) +(32.0*5.0)) * .1
	return y
	
def loadDictionary():
	for line in df:
		wordList.append(line)
		print line
		
def runSign(board):
	L = []
	
	try:
		Thread(target = inputThread, args=(L)).start()

	except:
		raise
		
	while True:
		
		for i in wordList:
			board.write(i)
			delay = float(board.readline())
			print i
			print getTime(delay)
			time.sleep(getTime(delay))
			if L:
				break
	
def main():
	loadDictionary()
	arduino = serial.Serial('/dev/ttyS0', 9600)
	
	runSign(arduino)
	
	df.close()
	return 0

if __name__ == '__main__':
	main()

