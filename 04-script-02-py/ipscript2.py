#!/usr/bin/env python3

import socket
import os

names = ["drive.google.com", "mail.google.com", "google.com"]
i = 0
n = 1
new_file = []
if os.path.exists("test.txt"):
	f = open("test.txt", "r+")
else:
	f = open("test.txt", "w+")

while i < len(names):
	ip = socket.gethostbyname(names[i])
	str_for_printing = names[i] + " - " + str(ip) + '\n'
	line = f.readline()
	if not line:
		#f.write(str_for_printing)
		print(str_for_printing)
		new_file.append(str_for_printing)
	elif line == str_for_printing:
		print(str_for_printing)
		new_file.append(str_for_printing)
	elif line != str_for_printing:
		line_lst = line.split()
		str_for_printing = "[ERROR] " + names[i] + " IP mismatch " + line_lst[2] + " " + str(ip) + '\n'
		print(str_for_printing)
		new_file.append(str_for_printing)
	i = i + 1
f.close()
f = open("test.txt", "w+")
f.writelines(new_file)
f.close()
