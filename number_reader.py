import json

file_name = 'numbers.json'

with open(file_name) as f_object:
	numbers = json.load(f_object)

print(numbers)