import json

#如果以前存储了用户名，就加载它
#否则，就提示用户输入用户名并存储它

def get_stored_user():
	"""如果存储了用户名，就获取它"""
	file_name = 'username.json'
	try:
		with open(file_name) as f_object:
			username = json.load(f_object)
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_username():
	"""提示用户输入用户名"""
	username = input('What is your name? ')
	file_name = 'username.json'
	with open(file_name, 'w') as f_object:
		json.dump(username, f_object)
	return username

def greet_user():
	"""问候用户，并指出其名字"""
	username = get_stored_user()
	if username:
		print('Welcome back, ' + username + '!')
	else:
		username = get_new_username()
		print("We'll remeber you when you come back, " + username + '!')

greet_user()