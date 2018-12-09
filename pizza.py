pizza = {
	'crust': 'thick',
	'toppings': ['mushroom', 'extra cheese'],
}

#概述点的比萨
print('You ordered a ' + pizza['crust'] + '-crust pizza ' +
	'with the following toppings:')
for topping in pizza['toppings']:
	print('\t' + topping)
	
def  make_pizza(size, *toppings):
	"""概述要制作的比萨"""
	print('\nMake a ' + str(size) +
		'-inch pizza with the folling toppings:')
	for topping in toppings:
		print('-' + topping)

make_pizza(16, 'peperoni')
make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')