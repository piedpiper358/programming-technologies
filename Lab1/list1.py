# -*- coding: utf-8 -*-


# 1. 
# Вх: список строк, Возвр: кол-во строк
# где строка > 2 символов и первый символ == последнему

def me(words):

  	return sum([1 for s in words if len(s)>2 and s[0] == s[-1] ])


# 2. 
# Вх: список строк, Возвр: список со строками (упорядочено)
# за искл всех строк начинающихся с 'x', которые попадают в начало списка.
# ['tix', 'xyz', 'apple', 'xacadu', 'aabbbccc'] -> ['xacadu', 'xyz', 'aabbbccc', 'apple', 'tix']


def fx(words):

	#return sorted(words, key=lambda str : '1'+str if str.startswith('x') else str)
	return sorted(words, key=lambda s : ('0', s) if s.startswith('x') else ('1', s))

	



# 3. 
# Вх: список непустых кортежей, 
# Возвр: список сортир по возрастанию последнего элемента в каждом корт.
# [(1, 7), (1, 3), (3, 4, 5), (2, 2)] -> [(2, 2), (1, 3), (3, 4, 5), (1, 7)]

def sorttuple(words):

	return sorted(words, key=lambda item: item[-1])
	# или words.sort(key=lambda item: item[-1]) 





#test(...)
def test(func, res, expt):

	print 'Function \''+str(func)+'\' supposed to return: ', expt	
	print ('and' if res == expt  else 'but') + ' returns:' , res




if __name__ == '__main__':
  #main()


	#test 1
	test('me', me(['f', 'oo', 'barb', 'aaaaaa', 'rrr']), 3);	
	#test 2
	test('fx', fx(['tix', 'xyz', 'apple', 'xacadu', 'aabbbccc']), ['xacadu', 'xyz', 'aabbbccc', 'apple', 'tix']);	
	#test 3
	test('sorttuple', sorttuple([(1, 7), (1, 3), (3, 4, 5), (2, 2)]), [(2, 2), (1, 3), (3, 4, 5), (1, 7)]);
	

