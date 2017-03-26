#!/usr/bin/python

import os
import sys

def OffASLR():
	os.system("echo \"0\" > /proc/sys/kernel/randomize_va_space")

def OnASLR():
	os.system("echo \"2\" > /proc/sys/kernel/randomize_va_space")

def StatASLR():
	f = open("/proc/sys/kernel/randomize_va_space","r")
	stat = f.read()
	f.close()
	if int(stat)==2:
		return True
	if int(stat)==0:
		return False 	

if __name__=="__main__":
	cmd = sys.argv[1]
	if cmd=="off":
		OffASLR()
		print "[INFO]Off Successed!"
	if cmd=="on":
		OnASLR()
		print "[INFO]On Successed!"
	if cmd=="status":
		r = StatASLR()
		if r==True:
			print "[Status]ASLR On!"
		if r==False:
			print "[Status]ASLR Off!"
	if cmd!="off" and cmd!="on" and cmd!="status":
		print "[ERROR]Unknown Command!"
