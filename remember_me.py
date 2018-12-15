import json

#如果以前存储了用户名，就加载它
#否则，就提示用户输入用户名并存储它

file_name = 'username.json'
try:
	with open(file_name) as f_object:
		username = json.load(f_object)
except FileNotFoundError:
	username = input('What is your name? ')
	with open(file_name, 'w') as f_object:
		json.dump(username, f_object)
		print("We'll remember you when you come back, " + username + '!')
else:
	print('Welcome back, ' + username + '!')
