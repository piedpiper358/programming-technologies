# -*- coding: utf-8 -*-

# 1. 
# Входящие параметры: int <count> , 
# Результат: string в форме
# "Number of: <count>", где <count> число из вход.парам.
#  Если число равно 10 или более, напечатать "many"
#  вместо <count>
#  Пример: (5) -> "Number of: 5"
#  (23) -> 'Number of: many'

def num_of_items(count):
  return 'Number of: ' +  ('many' if count>=10 else str(count))


# 2. 
# Входящие параметры: string s, 
# Результат: string из 2х первых и 2х последних символов s
# Пример 'welcome' -> 'weme'.
def start_end_symbols(s):
	return s[:2]+s[-2:]


# 3. 
# Входящие параметры: string s,
# Результат: string где все вхождения 1го символа заменяются на '*'
# (кроме самого 1го символа)
# Пример: 'bibble' -> 'bi**le'
# s.replace(stra, strb) 

def replace_char(s):
	return s[0] + s[1:].replace(s[0], '*')


# 4
# Входящие параметры: string a и b, 
# Результат: string где <a> и <b> разделены пробелом 
# а превые 2 симв обоих строк заменены друг на друга
# Т.е. 'max', pid' -> 'pix mad'
# 'dog', 'dinner' -> 'dig donner'
def str_mix(a, b):
  return b[:2] + a[2:] + ' ' + a[:2] + b[2:]


# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(func, res, expt):

  print 'Function \''+str(func)+'\' supposed to return: \'' + expt + '\'' 
  print ('and' if res == expt  else 'but') + ' returns: \'' + res + '\''

  


#test('start_end_symbols', start_end_symbols('welcome'), 'weme')
  
#test('replace_char', replace_char('bibble'), 'bi**le')



if __name__ == '__main__':
  #main()
  #test1 
  test('num_of_items', num_of_items(10), 'Number of: many')
  test('num_of_items', num_of_items(3), 'Number of: 3')
  #test2
  test('start_end_symbols', start_end_symbols('welcome'), 'weme')
  #test3
  test('replace_char', replace_char('bibble'), 'bi**le')
  #test4
  test('str_mix', str_mix('max', 'pid'), 'pix mad')
  test('str_mix', str_mix('dog', 'dinner'), 'dig donner')
