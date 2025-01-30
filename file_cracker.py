#/usr/bin/python3

# STATUS : WORKING

# CURRENT WORK : multi threading

# THINGS TO DO !!!

# Multi Threaded implementation
# implement john the ripper
# visual stuff
# finally add comments


import sys
import time
import os
import threading
from colorama import Style, Fore

class BruteForceCracker:
    def __init__(self, Dir, F_name):
        self.Dir = Dir
        self.F_name = F_name
        
        for run in banner:
            sys.stdout.write(run)
            sys.stdout.flush()
            time.sleep(0.02)
    
def password_cracker(Dir,F_name):
    
    os.chdir(Dir)
    stm_2 = f"cat {F_name}"
    os.system(stm_2)
    
    proceed_ask = input("Do you wish to bruteforce the file? (yes/no)")

	# let us go with gpg file locking and unlocking

    if proceed_ask == "yes":
        pswd_lst = passw()
        x = 0
	# os.system(f"touch decrypted_file.txt")

        while True:
            #time.sleep(0.5)
            pswd = pswd_lst[x].rstrip('\n')
            cmd = f"gpg --decrypt --batch --yes --passphrase {pswd} {F_name}"
            print(Fore.RED)
            print(f"Trying - {pswd}")
            print(Fore.WHITE)
            result = os.system(cmd)

            if(result == 0):
                print(Fore.BLUE)
                print(f"Correct password is : \n")
                print(Fore.GREEN)
                print(f"{pswd} \n")


                out_msg = "--------Thank you for using Brute-Forcer --------"

                for _ in out_msg:
                    sys.stdout.write(_)
                    sys.stdout.flush()
                    time.sleep(0.03)
                break
            
            x += 1
        
    elif proceed_ask == "no":
        banner = "------Thank you for using Brute-Forcer------\n" 
        for i in banner:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.05)
            
    else:
        print("PLEASE TRY AGAIN")
        password_cracker(Dir,F_name)
    
def main():
    Dir = input("Enter the Directory: ")
    F_name = input("Enter Filename: ")
    cracker = BruteForceCracker(Dir, F_name)
    password_cracker(Dir,F_name)
    
def passw():

    with open("passwords.txt", "r") as f:
        chunk_size = 1000
        while True:
            passwords = f.readlines(chunk_size)
            return passwords

if __name__ == '__main__':
    
    banner = "-------- Loading... -------- \n"
    print(Fore.RED)
    
    for i in banner:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.02)

    print(Fore.WHITE)

    main()
