# -*- coding: utf-8 -*-


# 1. 
# Вх: список чисел, Возвр: список чисел, где 
# повторяющиеся числа урезаны до одного 
# пример [0, 2, 2, 3] returns [0, 2, 3]. 

def rm_adj(nums):
	return list(set(nums)) 


# 2. Вх: Два списка упорядоченных по возрастанию, 
#	Возвр: новый отсортированный объединенный список 
  # return

def combine_list(list1, list2):
	#newlist = list(list1).copy()
	newlist = list1[:]
	newlist.extend(list2)
	#newlist.sort();

	#return sorted(list1[:].extend(list2))
	return sorted(newlist) 


#test(...)

def test(func, res, expt):

	print 'Function \''+str(func)+'\' supposed to return: ', expt	
	print ('and' if res == expt  else 'but') + ' returns:' , res





if __name__ == '__main__':
	#main()

	#test 1
	test('rm_adj', rm_adj([0, 2, 2, 3]), [0, 2, 3]);	
	#test 2
	test('combine_list', combine_list([17, 5, 7, 1], [2, 3, 5]), [1, 2, 3, 5, 5, 7, 17]);
	