#!/usr/bin/env python3

import socket
import os

def print_append_new_ip(new_ip, new_ip_list):
	print(new_ip)
	new_ip_list.append(new_ip)	
	return new_ip_list
	

names = ["drive.google.com", "mail.google.com", "google.com"]
i = 0
n = 1
nember_of_services = len(names)
new_ip_list = []
new_ip_json_list = []
new_ip_yaml_list = []
if os.path.exists("ip_services.txt"):
	f = open("ip_services.txt", "r+")
else:
	f = open("ip_services.txt", "w+")

while i < nember_of_services:
	old_ip = f.readline()
	ip = socket.gethostbyname(names[i])
	new_ip = names[i] + " - " + str(ip) + '\n'
	new_ip_for_yaml = "- " + names[i] + ": " + str(ip) + '\n'
	if (i + 1) != nember_of_services:
		new_ip_for_json = "\"" + names[i] + "\" : \"" + str(ip) + "\",\n"
	else:
		new_ip_for_json = "\"" + names[i] + "\" : \"" + str(ip) + "\""	
	if (not old_ip) or (old_ip == new_ip):
		new_ip_list = print_append_new_ip(new_ip, new_ip_list)
	elif old_ip != new_ip:
		old_ip_lst = old_ip.split()
		if old_ip_lst[0] !=  "[ERROR]":
			new_ip = "[ERROR] " + names[i] + " IP mismatch " + old_ip_lst[2] + " " + str(ip) + '\n'
		new_ip_list = print_append_new_ip(new_ip, new_ip_list)
	new_ip_json_list.append(new_ip_for_json)
	new_ip_yaml_list.append(new_ip_for_yaml)
	i = i + 1

f.close()
f = open("ip_services.txt", "w+")
f.writelines(new_ip_list)
f.close()
f = open("ip_services.json", "w+")
f.write("{ ") 
f.writelines(new_ip_json_list)
f.write(" }") 
f.close()
f = open("ip_services.yml", "w+")
f.write("---\n") 
f.writelines(new_ip_yaml_list)
f.write("...") 
f.close()
