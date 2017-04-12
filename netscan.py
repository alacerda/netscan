#!/usr/bin/python

import sys
import socket

if len(sys.argv) != 3:
	quit()

alvo = sys.argv[1]
portas = sys.argv[2]

class Sock:
	def __init__(self, target, port):
		self.target = target
		self.port = port

def scan(sock):
	s = socket.socket()
	try:
		s.connect((sock.target, sock.port))
		print "\tListening on port: %d"%sock.port
	except socket.error:
		pass
	finally:
		s.close()

print "Scanning for open ports on: %s"%alvo

for porta in range(int(portas.split("-")[0]),int(portas.split("-")[1]) + 1):
	scan(Sock(alvo,porta))
