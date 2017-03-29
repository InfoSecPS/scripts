from socket import *
import os
from termcolor import colored
import sys

os.system('clear')

ip = sys.argv[1]
head = "HEAD / HTTP/1.0\r\n\r\n"
get = "GET / HTTP/1.0\r\n\r\n"
options = "OPTIONS / HTTP/1.0\r\n\r\n"

print "  "
print colored ('[*] ', 'green') + "Http Banner grab for :" + ip

def first():
	print colored ('[*] ', 'green') + "HEADER Response"
	try:
		s = socket(AF_INET, SOCK_STREAM)
		s.connect((ip,80))
		s.send(head)
		print s.recv(1024)
		s.close()
	except:
		print 'HEADER request error'

def second():
	print colored ('[*] ', 'green') + "GET Request response"
        try:
                s = socket(AF_INET, SOCK_STREAM)
                s.connect((ip,80))
                s.send(get)
                print s.recv(1024)
                s.close()
        except:
                print 'GET request error'

def third():
	print colored ('[*] ', 'green') + "OPTIONS Response"
        try:
                s = socket(AF_INET, SOCK_STREAM)
                s.connect((ip,80))
                s.send(options)
                print s.recv(1024)
                s.close()
        except:
                print 'OPTIONS request error'

print " "
first()
print " "
second()
print " "
third()

