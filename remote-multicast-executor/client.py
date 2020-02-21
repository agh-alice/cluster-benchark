#!/bin/python3
import socket
import sys
import functools

UDP_IP = "224.0.70.71"
UDP_PORT = 7070
MESSAGE = functools.reduce(lambda x, y: x + " " + y, sys.argv[1:]).encode()
 
print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)
print("message:", MESSAGE)
 
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
