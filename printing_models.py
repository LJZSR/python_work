def print_models(unprinted_designs, complete_models):
	"""
	模拟打印每个设计，直到没有未打印的设计为止
	打印每个设计后，都将其移到列表complete_models中
	"""
	while unprinted_designs:
		current_design = unprinted_designs.pop()

		#模拟根据设计制作3D打印模型的过程
		print('Printing model: ' + current_design)
		complete_models.append(current_design)

def show_completed_models(complete_models):
	"""显示打印好的所有模型"""
	print('\nThe following models have been printed:')
	for complete_model in complete_models:
		print(complete_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
complete_models = []

print_models(unprinted_designs, complete_models)
show_completed_models(complete_models)