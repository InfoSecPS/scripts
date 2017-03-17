#!/bin/python2

import optparse
from socket import *
from threading import *
from termcolor import colored
import os
import time

#clears the terminal window
os.system('cls||clear')

screenLock = Semaphore(value=1)

print '\n' + colored ("[+] Scan started: ", "yellow") + time.strftime("%c") + '\n'

def connScan(tgtHost, tgtPort):
	try:
		connSkt = socket(AF_INET, SOCK_STREAM)
		connSkt.connect((tgtHost, tgtPort))
		connSkt.send('hello\r\n')

		results = connSkt.recv(1024)
		screenLock.acquire()
		print colored ('[+] ','green') + str(tgtPort) + "/tcp Open"
	except:
		screenLock.acquire()
		print colored ('[-] ','red') + str(tgtPort) + "/tcp Closed"
	finally:
		screenLock.release()
		connSkt.close()

def portScan(tgtHost, tgtPorts):
	try:
		tgtIP = gethostbyname(tgtHost)
	except:
		print "[-] Cannot resolve " + tgtHost + ": Uknown host"
		return

	try:
		tgtName = gethostbyaddr(tgtIP)
		print "\n" + colored ('[+] Scan Results for: ','yellow') + tgtName[0] + '\n'
	except:
		print "\n" + colored ('[+] Scan Results for: ','yellow') + tgtIP + '\n'

	setdefaulttimeout(1)
	for tgtPort in tgtPorts:
		t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
		t.start()

def Main():
	parser = optparse.OptionParser('usage %prog -H <target host> '+\
		'-p <target port>')
	parser.add_option('-H', dest='tgtHost', type='string', \
		help='specifiy target host')
	parser.add_option('-p', dest='tgtPort', type='string', \
		help='specifiy targetport[s] seperated by a comma')
	(options, args) = parser.parse_args()
	if (options.tgtHost == None) | (options.tgtPort == None):
		print parser.usage
		exit(0)
	else:
		tgtHost = options.tgtHost
		tgtPorts = str(options.tgtPort).split(',')

	portScan(tgtHost, tgtPorts)

if __name__ == '__main__':
		Main()
