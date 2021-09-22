# -*- coding: utf-8 -*-


"""
Прочитать из файла (имя - параметр командной строки)
все слова (разделитель пробел)

Создать "Похожий" словарь который отображает каждое слово из файла
на список всех слов, которые следуют за ним (все варианты).

Список слов может быть в любом порядке и включать повторения.
например "and" ['best", "then", "after", "then", ...] 

Считаем , что пустая строка предшествует всем словам в файле.

С помощью "Похожего" словаря сгенерировать новый текст
похожий на оригинал.
Т.е. напечатать слово - посмотреть какое может быть следующим 
и выбрать случайное.

В качестве теста можно использовать вывод программы как вход.парам. для следующей копии
(для первой вход.парам. - файл)

Файл:
He is not what he should be
He is not what he need to be
But at least he is not what he used to be
  (c) Team Coach

"""

import random
import sys
import re



from collections import defaultdict
import string

def mem_dict(filename):

	try:
		f = open(filename, 'r')
	except IOError as e:
		print(u'не удалось открыть файл')
	else:
		translator = str.maketrans('', '', string.punctuation)

		result = defaultdict(list)

		#y = f.read().lower().replace('\n', ' ').split(".!?")
		x = re.sub(r'[.!?]','\n', f.read().lower().replace('\n', ' ')).translate(translator).split('\n')

		for line in x:
			y = line.split()
			#y = line.lower().translate(translator).replace('\n', '').split()
			#y = line.lower().translate(translator).replace('\n', '').replace('.', '\n').split()
			#for i, j in zip(y[:], y[1:]):
			#	result[i].append(j)
				#result.get(i, list()).append(j)
			for i in range(len(y)):
				for j in range(i+1,len(y)):
					#result[y[i]].append(y[j])

					result[y[i]] = result.get(y[i], list()) + [y[j]]
					#result[y[i]]
				#print(result[y[i]])	
				if i!=len(y)-1:
					element = random.choice(result[y[i]])
					print(element, end=' ')
				else:
					element = random.choice(list(result))
					print(element)


		#print(result)

		#element = random.choice(list(result))
		#print(element, end=' ')

		#while result[element]:
		#	element = random.choice(list(result[element]))
		#	print(element, end=' ')
		#print()
		f.close()
	return



if __name__ == '__main__':
	mem_dict('file')
