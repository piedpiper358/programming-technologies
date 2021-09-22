# -*- coding: utf-8 -*-

# 1. 
# �������� ���������: int <count> , 
# ���������: string � �����
# "Number of: <count>", ��� <count> ����� �� ����.�����.
#  ���� ����� ����� 10 ��� �����, ���������� "many"
#  ������ <count>
#  ������: (5) -> "Number of: 5"
#  (23) -> 'Number of: many'

def num_of_items(count):
  return 'Number of: ' +  ('many' if count>=10 else str(count))


# 2. 
# �������� ���������: string s, 
# ���������: string �� 2� ������ � 2� ��������� �������� s
# ������ 'welcome' -> 'weme'.
def start_end_symbols(s):
	return s[:2]+s[-2:]


# 3. 
# �������� ���������: string s,
# ���������: string ��� ��� ��������� 1�� ������� ���������� �� '*'
# (����� ������ 1�� �������)
# ������: 'bibble' -> 'bi**le'
# s.replace(stra, strb) 

def replace_char(s):
	return s[0] + s[1:].replace(s[0], '*')


# 4
# �������� ���������: string a � b, 
# ���������: string ��� <a> � <b> ��������� �������� 
# � ������ 2 ���� ����� ����� �������� ���� �� �����
# �.�. 'max', pid' -> 'pix mad'
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
