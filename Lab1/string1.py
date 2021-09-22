
# -*- coding: utf-8 -*-

# 1. 
# Вх: строка. Если длина > 3, добавить в конец "ing", 
# если в конце нет уже "ing", иначе добавить "ly".
def v(s):

	#if len(s)>3 and s.endswith('ing'):	
	#	s = s + 'ing'
	#else: 
	#	s = s + 'ly'

  	#return s

  	return s + 'ing' if len(s)>3 and not s.endswith('ing') else s + 'ly'
  	


# 2. 
# Вх: строка. Заменить подстроку от 'not' до 'bad'. ('bad' после 'not')
# на 'good'.
# Пример: So 'This music is not so bad!' -> This music is good!

def nb(s):
	start = s.find('not')

	stop = s.find('bad', start)

	if start != -1 and stop != -1:
		s=s[:start] + 'good' + s[stop+3:]
  	return s



# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(func, res, expt):

  print 'Function \''+str(func)+'\' supposed to return: \'' + expt + '\'' 
  print ('and' if res == expt  else 'but') + ' returns: \'' + res + '\''



if __name__ == '__main__':
  #main()
  #test1 
  test('v', v('ling'), 'lingly')
  test('v', v('lightning'), 'lightningly')
  #test2
  test('nb', nb('This music is not so bad!'), 'This music is good!')
