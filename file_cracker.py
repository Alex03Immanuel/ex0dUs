#/usr/bin/python3

# THINGS TO DO !!!
# Fore.RED change
# File Locking check
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
    def __init__(self, Dir, F_name, error):
        self.Dir = Dir
        self.F_name = F_name
        self.error = error
        
        for run in banner:
            sys.stdout.write(run)
            sys.stdout.flush()
            time.sleep(0.02)
    
def password_cracker(Dir,F_name):
    
    os.chdir(Dir)
    stm_2 = 'cat '+F_name
    os.system(stm_2)
    
    proceed_ask = input("Do you wish to bruteforce the file? (yes/no)")
    
    if proceed_ask == "yes":
        pswd_lst = passw()
        x = 0
        while x<10:
            time.sleep(0.5)
            pswd = pswd_lst[x].rstrip('\n')
            cmd = "unar -p "+pswd +" "+F_name
            print(cmd)
            os.system(cmd)
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

    print(Fore.RED)
    Dir = input("Enter the Directory: ")
    F_name = input("Enter Filename: ")  
    error = input("Enter Wrong Password Error Message: ")
    cracker = BruteForceCracker(Dir, F_name, error)
    password_cracker(Dir,F_name)
    
def passw():

    with open("passwords.txt", "r") as f:
        chunk_size = 1000
        while True:
            passwords = f.readlines(chunk_size)
            return passwords

if __name__ == '__main__':
    banner = "Loading...\n"
    print(banner)
    main()
