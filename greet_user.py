import json

file_name = 'username.json'

with open(file_name) as f_object:
	username = json.load(f_object)
	print('Welcome back, ' + username + '!')