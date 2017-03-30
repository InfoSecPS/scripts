import argparse
from socket import *
import os

os.system('clear')

def connect(tgtHost):
	try:
		connSkt = socket(AF_INET, SOCK_STREAM)
		connSkt.connect((tgtHost,80))
		connSkt.send('GET / HTTP/1.1\r\n\r\n')

		result = connSkt.recv(2048)
		print(result)
	except:
		print "No connection to: " + tgtHost
		connSkt.close()


def main():
	parser = argparse.ArgumentParser('argparse.py -H <target host>')
	parser.add_argument('-H', dest='tgtHost', type=str, help='specify target IP')

	args = parser.parse_args()

	if args.tgtHost is None:
		parser.print_help()
	else:
		connect(args.tgtHost)

if __name__ == '__main__':
	main()
