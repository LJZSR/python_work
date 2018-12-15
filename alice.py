file_name = 'alice.txt'

try:
	with open(file_name) as file_object:
		contents = file_object.read()
except FileNotFoundError:
	msg = 'Sorry, the file ' + file_name + ' does not exist!'
	print(msg)
else:
	#计算文件大致包含多少单词
	words = contents.split()
	num_words = len(words)
	print('The file ' + file_name + ' has about ' + str(num_words) + ' words.')
