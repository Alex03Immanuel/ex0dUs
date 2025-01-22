#!/usr/bin/python3

import sys
import os
import time

flag = False

print("___ Enter the user name ___ \n")
U_name = input("username:")


def pas():
	os.chdir('/home/alex/Documents/Hacking')
	with open ("passwords.txt","r") as f :
		chunk_size = 1000
		while True:
			password = f.readlines(chunk_size)
			return password

print("""




			_____BRUTEFORCER STARTING_____		

								""" )

stm = "nmcli device wifi connect"

pswd_lst = pas()
x = 0

while (x < 1000):
	time.sleep(0.1)
