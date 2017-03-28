from socket import *
import os

os.system('cls||clear')

ip = "192.168.187.139" #change this obviously
head = "HEAD / HTTP/1.0\r\n\r\n"
get = "GET / HTTP/1.0\r\n\r\n"
options = "OPTIONS / HTTP/1.0\r\n\r\n"

def first():
	try:
		s = socket(AF_INET, SOCK_STREAM)
		s.connect((ip,80))
		s.send(head)
		print s.recv(1024)
		s.close()
	except:
		print 'HEADER request error'

def second():
        try:
                s = socket(AF_INET, SOCK_STREAM)
                s.connect((ip,80))
                s.send(get)
                print s.recv(1024)
                s.close()
        except:
                print 'GET request error'

def third():
        try:
                s = socket(AF_INET, SOCK_STREAM)
                s.connect((ip,80))
                s.send(options)
                print s.recv(1024)
                s.close()
        except:
                print 'OPTIONS request error'

first()
second()
third()
