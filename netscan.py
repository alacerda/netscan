#!/usr/bin/python

import sys
import socket
import time
from threading import Thread, current_thread

if len(sys.argv) != 3:
	quit()

THREADS = 5

alvo = sys.argv[1]
portas = sys.argv[2]
porta_starts = int(portas.split("-")[0])
porta_ends = int(portas.split("-")[1])
total_portas = len(range(porta_starts,porta_ends))

class Sock(Thread):
	def __init__(self, alvo, porta_start, porta_end):
		Thread.__init__(self)
		self.alvo = alvo
		self.porta_start = porta_start
		self.porta_end = porta_end

	def run(self):
		for p in range(self.porta_start,self.porta_end):
			s = socket.socket()
			try:
				s.connect((self.alvo, p))
				sys.stdout.write("\t" + current_thread().name +" found open port: " +str(p)+"\n")
				sys.stdout.flush()
			except socket.error:
				pass
			finally:
				s.close()

print "Scanning for open ports on: %s"%alvo

if total_portas < THREADS:
	if len(range(porta_starts,porta_ends)) == 0:
		s = socket.socket()
                try:
                        s.connect((alvo, porta_starts))
                        sys.stdout.write("\tListening on port: "+str(porta_starts)+"\n")
			sys.stdout.flush()
                except socket.error:
                        pass
                finally:
                        s.close()
	else:
		for porta in range(porta_starts,porta_ends):
			s = socket.socket()
        		try:
                		s.connect((alvo, porta))
				sys.stdout.write("\tListening on port: "+str(porta)+"\n")
	                        sys.stdout.flush()
        		except socket.error:
                		pass
		        finally:
        		        s.close()
else:
	for i in range(1,(THREADS + 1)):
       		start = porta_starts
	        next_end_port = (start + (total_portas / THREADS))
	
       		if next_end_port < porta_ends:
                	end = next_end_port
	       	        porta_starts = end +1
        	else:
       	        	end = porta_ends
	
		my_sock = Sock(alvo,start,end)
		my_sock.start()
	
       		if end == porta_ends:
			quit()

