def describe_pet(animal_tpye, pet_name):
	"""显示宠物信息"""
	print('\nI have a ' + animal_tpye + '.')
	print('My ' + animal_tpye + "'s name is " + pet_name.title() + '.')

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')