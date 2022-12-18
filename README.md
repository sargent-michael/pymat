# PyMat.py 

PyMat is a simple CTF project directory automation tool. Often times, I find myself creating a directory, then cd'ing into, and then being able to start my enumeration workflow. This script is to help with that. Right now it is a little bare-bones because it just creates a project directory in the the CTF platform directory that you are using at that time. You can also list the current project folders in those CTF folders with the -l option.

**PLEASE NOTE:** In order for this script to work for you, you need to create a htb (hack-the-box)and thm (try-hack-me) directory in your documents folder as well as replacing the directory on lines 14 and 28 to your users documents directory.

## Example of Usuage
Let's take a look at the the help menu.
```python
./pymat.py -h
usage: pymat.py [-h] [-c] [-l] [-p]

Simple Python Port Scanner

options:
  -h, --help       show this help message and exit
  -c , --ctf       ctf platform - i.e. "hack the box" or "try hackme"
  -l , --list      list the contents of a CTF Directory
  -p , --project   the name of target machine
```

First, lets try htb and project Test...
```python
./pymat.py -c htb -p Test  
[+] Validating CTF Platform
[+] Checking to see if that directory already exists
[+] Creating a new directory for htb
[+] Directory creation was successful
```

Now lets re-run it to see what we get...
```python
./pymat.py -c htb -p Test
[+] Validating CTF Platform
[+] Checking to see if that directory already exists
[-] That project already exists...
```

As you can see here, we inputted an incorrect CTF Platform and got an error
```python
./pymat.py -c adf -p Test
[+] Validating CTF Platform
[-] Platform "adf" does not exist...
```

List of htb Projects
```python
./pymat.py -l htb          
[+] Checking for htb project folders
[+] Printing htb project folders...

shoppy
support
```

List error
```python
./pymat.py -l adsf
[+] Checking for adsf project folders
[-] Platform "adsf" does not exist...
```