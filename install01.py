import subprocess
import os
import sys

try:
    subprocess.check_output(["virtualenv", "--version"])
except OSError:
    print "No such program `virtualenv`"
    sys.exit(0)

if not os.path.isdir("env"):
    subprocess.call(["virtualenv", "env"])
    print "env created"
else:
    print "env exists"

subprocess.call(["pip", "install", "-r", "requirements.txt"])
print "requirements installed"
    