#!/usr/bin/python3
import argparse
import os
from colorama import Fore


def main():
    # Arguments
    parser = argparse.ArgumentParser(description='Simple Python Port Scanner')
    parser.add_argument('-c', '--ctf', action="store", dest="ctf", help='ctf platform - i.e. \"hack the box\" or \"try hackme\"', metavar='', required=True)
    parser.add_argument('-p', '--project', action="store", dest="project", help='the name of target machine', metavar='', required=True)

    # Args to Vars
    args = parser.parse_args()
    platform = args.ctf
    project = args.project
    
    print("[+] Validating CTF Platform")

    if platform == 'htb' or platform == 'thm':

        print("[+] Checking to see if that directory already exists")
        dir_check = os.path.exists(f'/home/nop/Documents/{platform}/{project}')
        
        if dir_check == False:
            if platform == 'htb':
                print("[+] Creating a new directory for htb")
                os.system(f"mkdir ~/Documents/htb/{project}")
                print(Fore.GREEN + "[+] Directory creation was successful")

            elif platform == 'thm':
                print("[+] Creating a new directory for thm")
                os.system(f"mkdir ~/Documents/thm/{project}")
                print(Fore.GREEN + "[+] Directory creation was successful")

        else:
                print(Fore.RED + "[-] That project already exists...")

    else:
        print(Fore.RED + f"[-] Platform \"{platform}\" does not exist...")
        

if __name__ == "__main__":
    main()  