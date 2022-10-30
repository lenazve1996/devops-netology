#!/usr/bin/env python3

import socket
import os

names = ["drive.google.com", "mail.google.com", "google.com"]
i = 0
n = 1
new_ip_list = []
if os.path.exists("test.txt"):
	f = open("test.txt", "r+")
else:
	f = open("test.txt", "w+")

while i < len(names):
	ip = socket.gethostbyname(names[i])
	new_ip = names[i] + " - " + str(ip) + '\n'
	old_ip = f.readline()
	if not old_ip:
		print(new_ip)
		new_ip_list.append(new_ip)
	elif old_ip == new_ip:
		print(new_ip)
		new_ip_list.append(new_ip)
	elif old_ip != new_ip:
		old_ip_lst = old_ip.split()
		new_ip = "[ERROR] " + names[i] + " IP mismatch " + old_ip_lst[2] + " " + str(ip) + '\n'
		print(new_ip)
		new_ip_list.append(new_ip)
	i = i + 1
f.close()
f = open("test.txt", "w+")
f.writelines(new_ip_list)
f.close()
