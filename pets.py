def describe_pet(pet_name, animal_tpye='dog'):
	"""显示宠物信息"""
	print('\nI have a ' + animal_tpye + '.')
	print('My ' + animal_tpye + "'s name is " + pet_name.title() + '.')

describe_pet('harry', 'hamster')
describe_pet('willie')