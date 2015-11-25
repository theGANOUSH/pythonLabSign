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
import datetime
import socket
import fcntl
import struct
import serial
import time
from threading import Thread

wordList = []
weekday = {0: "Welcome Back Monday", 1: "Pop Tuesday", 2: "Blues Wednesday", 3: "Throwback Thursday!", 4: "Rocking Friday"};
    

def returnFloat(a):
    return float(a)
    
def scanWeek():
    today = datetime.datetime.today().weekday()
    yesterday = today - 1
    
    if(yesterday == -1):
        yesterday = 4
    i = 0
    for line in wordList:
        if(wordList[i] == weekday[yesterday]):
            wordList[i] = weekday[today]
        i += 1

def getIpAddress(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(s.fileno(),0x8915, struct.pack('256s', ifname[:15]))[20:24])

df = open("Dictionary.txt", "r+")

def getTime(x):
	y = float((float(x) +(32.0*5.0)) * .1)
	return y
	
def loadDictionary():
	for line in df:
		wordList.append(line)
		print line

def runSign(board):
	while True:
		for i in wordList:
			board.write(i)
			delay = board.readline()
			time.sleep(getTime(float(delay)))
			scanWeek()
						
def main():
	wordList.append(getIpAddress('eth0'))
	wordList.append(weekday[1])
		
	loadDictionary()
	arduino = serial.Serial('/dev/ttyS0', 9600)
	
	runSign(arduino)
	
	df.close()
	return 0

if __name__ == '__main__':
	main()

