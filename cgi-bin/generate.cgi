#!/usr/bin/python
import os
import sys

print("Content-Type: text/html")
print("")
print("<!DOCTYPE html>")
print("<html>")
print("<body>")

for param in os.environ:
    print("{p_name:20}: {p_value:20} <br>".format(p_name=param, p_value=os.environ[param]))

print('*************<br>')

for line in sys.stdin.read():
    print(line)
print("</body>")
print("</html>")