#!/usr/bin/python3
import argparse
import os
from colorama import Fore


def list_all(dir_list):
    # Prints all CTF project folders
    print(f"[+] Printing all project folders...")
    
    print("[+] Hack-the-Box Projects")
    htb_dir = os.listdir('/<USER>/<PATH>/Documents/htb/')
    for i in htb_dir:
        print(f"\t{i}") 
    
    print("[+] Try-Hack-Me Projects")
    thm_dir = os.listdir('/<USER>/<PATH>/Documents/thm/')
    for i in thm_dir:
        print(f"\t{i}")


def list_dir(dir_list):  
    # Checks for valid CTF folder
    print(f"[+] Checking for {dir_list} project folders")
    if dir_list == 'htb' or dir_list == 'thm':
        # List the project folder in that Directory
        print(f"[+] Printing {dir_list} project folders...")
        ctf_dir = os.listdir(f'/<USER>/<PATH>/Documents/{dir_list}')
        for i in ctf_dir:
            print(f"\t{i}")   
    
    # If the user does not input a correct ctf, then it will exit out...
    else:
       print(Fore.RED + f"[-] Platform \"{dir_list}\" does not exist...")

def make_dir(platform, project):
    print("[+] Validating CTF Platform")
    # Checks to see if the user entered a correct CTF Platform
    if platform == 'htb' or platform == 'thm':
        # Checks to see if the path already exists
        print("[+] Checking to see if that directory already exists")
        dir_check = os.path.exists(f'/<USER>/<PATH>/Documents/{platform}/{project}')

        # If the path does not already exist then it will continue
        if dir_check == False:
            # Generates a new CTF Project in the given CTF dir
            if platform == 'htb':
                print("[+] Creating a new directory for htb")
                os.system(f"mkdir ~/Documents/htb/{project}")
                print(Fore.GREEN + "[+] Directory creation was successful")
            elif platform == 'thm':
                print("[+] Creating a new directory for thm")
                os.system(f"mkdir ~/Documents/thm/{project}")
                print(Fore.GREEN + "[+] Directory creation was successful")
        
        # If that dir already exists, then it will exit out...
        else:
                print(Fore.RED + "[-] That project already exists...")
    
    # If the user does not input a correct ctf, then it will exit out...
    else:
       print(Fore.RED + f"[-] Platform \"{platform}\" does not exist...")


def main():
    # Arguments
    parser = argparse.ArgumentParser(description='Simple CTF Project Manager')
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS, help='\b\b\b\bShow this help message and exit.')
    parser.add_argument('-c', '--ctf', action="store", dest="ctf", help='ctf platform - i.e. \"hack the box\" or \"try hackme\"', metavar='\b')
    parser.add_argument('-l', '--list', action="store", dest="list", help='list the contents of a CTF Directory', metavar='\b')
    parser.add_argument('-p', '--project', action="store", dest="project", help='the name of target machine', metavar='\b')

    # Args to Vars
    args = parser.parse_args()
    dir_list = args.list
    platform = args.ctf
    project = args.project

    # Determines what to do
    if project is not None:
        make_dir(platform, project)
    elif dir_list is not None:
        if dir_list == 'all':
            list_all(dir_list)
        else:
            list_dir(dir_list)
    else:
        parser.print_help()
       

if __name__ == "__main__":
    main()  
