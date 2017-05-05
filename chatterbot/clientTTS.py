#!/usr/bin/env python
# coding: utf-8

import socket
import sys

hote = "localhost"
port = 15555

chaine = ""
tab = sys.argv[1].split("_");
for i in tab :
	chaine+=i+" "

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))
print "Connection on {}".format(port)

socket.send(chaine)

# while 1:
# 		data = socket.recv(1024)
# 		if data:
# 			print data

# 			break

print "Close"
socket.close()