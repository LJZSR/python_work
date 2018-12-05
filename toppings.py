available_toppings = ['mushrooms', 'olives', 'green peppers', 
					  'pepperoni', 'pineapple', 'extra chess']

requested_toppings = ['mushrooms', 'french fries', 'extra chess']

for requested_topping in requested_toppings:
	if requested_topping not in available_toppings:
		print('Sorry, we are out of ' + requested_topping + ' right now.')
	else:
		print('Adding ' + requested_topping + '.')
print('\nFinished making your pizza!')