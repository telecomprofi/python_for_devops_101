#!/usr/bin/env python3
from subprocess import PIPE, run, Popen

# simple use without pipes, greps etc

command = ['ls', '-l']
result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True)
print(result.returncode, result.stdout, result.stderr)

import subprocess

# more complex with pipes, greps
cmd = "ps -A|grep --color '[j]ava'"
ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
output = ps.communicate()[0]
print(output)
