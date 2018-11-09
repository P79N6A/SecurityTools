#!/usr/bin/env python3
#cording = utf-8

#from pwn import *

import subprocess
import shlex
import sys

file1 = sys.argv[1]
file2 = sys.argv[2]

command_line = "diff  {} {}".format(file1, file2)
command_args = shlex.split(command_line)

rc = 0
try:
    rc = subprocess.check_output(command_args)
except subprocess.CalledProcessError as cpe:
    print("shell returncode is not 0.")
    print("returncode: {}".format(cpe.returncode))
    print("output: {}".format(cpe.output))
    rc = cpe.returncode

print(rc)


'''
def convert(string):  # convert file to 16 byte
    convertfile =""
    for w in string:
        w = hex(w)
        convertfile += w
    return convertfile
'''

'''
def Caeser(string, shift): # this is caeser program
    save = ''
    for s in string:
        s = ord(s)
        if 65 <= s and s <= 90:
            s = s + shift
            if s > 90
               zurasu = s - 90
               s = 65 + zurasu
        elif 97 <= s and 122 >= s :
            s = s + shift
            if s > 122:
               zura = s - 122
               s = s + zura
        s = chr(s)
        save += s
    return save

#compare program list


f1 = open("./filename1","r") #Designation file 1
string1 = f1.read()
binary1 = convert(string1)

f2 = open("./filename2","r") #Designation file 2
string2 = f2.read()
binary2 = convert(string2)
  

print(binary1)
print(binary2)
'''
