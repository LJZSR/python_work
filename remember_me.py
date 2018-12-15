import json

username = input('What is your name? ')

file_name = 'username.json'
with open(file_name, 'w') as f_object:
	json.dump(username, f_object)
	print("We'll remember you when you come back, " + username + '!')
