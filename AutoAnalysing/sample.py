#!/usr/bin/env python3
#cording = utf-8

import subprocess
import sys

'''
cmd = "ls -l"
res = subprocess.call(cmd.split())
print(res)
'''

file1 = sys.argv[1]
command_line = "hexdump -C {}".format(file1)
res = subprocess.call(command_line)
print(res)