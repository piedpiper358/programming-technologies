"""
Вход: файл guess.txt содержащий имена для угадывания 

(например из http://www.biographyonline.net/people/famous-100.html можно взять имена)


Написать игру "Угадай по фото"

3 уровня сложности:
1) используются имена только 1-10
2) имена 1-50
3) имена 1-100

- из используемых имен случайно выбрать одно
- запустить поиск картинок в Google по выбранному
- получить ~30-50 первых ссылок на найденные по имени изображения
- выбрать случайно картинку и показать ее пользователю для угадывания
  (можно выбрать из выпадающего списка вариантов имен)
- после выбора сказать Правильно или Нет

п.с. сделать серверную часть, т.е. клиент играет в обычном браузере обращаясь к веб-серверу.

п.с. для поиска картинок желательно эмулировать обычный пользовательский запрос к Google
или можно использовать и Google image search API

goole custom search

https://ajax.googleapis.com/ajax/services/search/images? или др. варианты
НО в случае API нужно предусмотреть существующие ограничения по кол-ву запросов
т.е. кешировать информацию на случай исчерпания кол-ва разрешенных (бесплатных) запросов или другим образом обходить ограничение. 
Т.е. игра не должна прерываться после N запросов (ограничение API)


п.с. желательно "сбалансировать" параметры поиска (например искать только лица, 
использовать только первые 1-30 найденных и т.п.)
для минимизации того что найденная картинка не соответствует имени




p.s. Отчет также высылать на xms@npp-itb.spb.ru
"""

import random
import sys
import re



from collections import defaultdict
import string

from urllib import request
from urllib.parse import quote

import requests

from urllib.request import urlopen
from lxml import html
from lxml import etree

import urllib.request
import urllib.parse

def guess_who(filename):
	print("Content-type: text/html")
	print()
	print("<h1>Hello world!</h1>")


	try:
		f = open(filename, 'r')
	except IOError as e:
		print(u'не удалось открыть файл')
	else:
		#translator = str.maketrans('', '', string.punctuation)

		fam_list=list()
		for line in f:
			#занести в словарь  список
			fam_list.append(line.replace('\n', ''))

		searchTerm = random.choice(fam_list)
		print(searchTerm)


		#searchTerm = searchTerm.replace(' ','%20')


		

		

		
		#r = requests.get(url, headers = headers)

		#tree = html.fromstring(r.text)
		#r = tree.xpath('//div[@class = "y yi"]')[0]
		#print(r)
		#print(r.text)

		#print(etree.tostring(r))
		#with open('test3.html', 'w') as output_file:
			#output_file.write(etree.tostring(r))

		#i=0
		#imageName = urllib.parse.urlencode(searchTerm)
		#requestURL = 'http://images.google.ru/images?%s&hl=ru&start=%d' % (imageName,i)

		#requestURL = "https://www.google.ru/search?q={0}&tbm=isch".format(quote(searchTerm))
		#requestHeaders = {'User-Agent':'Mozilla/5.0'}


		#request = urllib.request.Request(requestURL, None, requestHeaders)
		#htmlPage = urllib.request.urlopen(request).read(500000)
		#htmlPage=str(htmlPage)
		#print(htmlPage)

		#with open('test3.html', 'w') as output_file:
		#	output_file.write(htmlPage)

		#requestURL = "https://www.google.ru/search?q={0}&tbm=isch".format(quote(searchTerm))
		requestURL = "https://www.google.ru/search?newwindow=1&q={0}&tbm=isch".format(quote(searchTerm))
		
		#requestHeaders = {'User-Agent':'Mozilla/5.0'}
		requestHeaders = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/70.0.3538.77 Chrome/70.0.3538.77 Safari/537.36'}


		request = urllib.request.Request(requestURL, None, requestHeaders)
		htmlPage = urllib.request.urlopen(request)
		#page = urlopen('https://docs.python.org/3/library/urllib.request.html')



		tree = html.fromstring(htmlPage.read())
		root = tree.xpath('//div[@class = "y yi"]')[0]
		#print(r)
		#print(r.text)


		#tree.xpath('//div[@class = "y yi"]/div[@class = "rg_bx rg_di rg_el ivg-i"]')[0]
		root = tree.xpath('//div[@class = "y yi"]/div[@class = "rg_bx rg_di rg_el ivg-i" and @data-ri = "2"]')[0]




		print(etree.tostring(root))
		with open("test3.html", "wb") as output_file:
		    output_file.write(etree.tostring(root))
		output_file.close()






		#fetcher = urllib2.build_opener()
		#searchTerm = 'parrot'
			#startIndex = 0
		
		#html = urlopen(searchUrl)
		#print(html.read())

		#out = open('a.html', 'bw')
		#out.write(html.read())
		

		
		#f = fetcher.open(searchUrl)
		#deserialized_output = simplejson.load(f)


		#print()
		f.close()
		return



#test(...)
def test(func, res, expt):

	#print 'Function \''+str(func)+'\' supposed to return: ', expt	
	#print ('and' if res == expt  else 'but') + ' returns:' , res
	return




if __name__ == '__main__':
	#main()
	guess_who('file')






#<div jscontroller="Q7Rsec" data-ri="0" class="rg_bx rg_di rg_el ivg-i" data-ved="0ahUKEwid2rmyrYffAhVqoYsKHaT-DakQMwg5KAAwAA"><a jsname="hSRGPd" href="#" target="_blank" jsaction="fire.ivg_o;mouseover:str.hmov;mouseout:str.hmou" class="rg_l" rel="noopener"><div class="THL2l"></div><img class="rg_ic rg_i" id="Zqxe7AJ5kXGqSM:" jsaction="load:str.tbn" alt="Картинки по запросу Nelson Mandela" onload="typeof google==='object'&&google.aft&&google.aft(this)"><div class="rg_ilmbg"> 219&nbsp;&#215;&nbsp;274  </div></a><a class="iKjWAf a-no-hover-decoration irc-nic isr-rtc" href="#" jsaction="mouseover:m8Yy5c;mousedown:QEDpme;focus:QEDpme;" rel="noopener" target="_blank"><div class="mVDMnf nJGrxf">Мандела, Нельсон — Википедия</div><div class="nJGrxf FnqxG">ru.wikipedia.org</div></a><div class="rg_meta notranslate">{"cb":21,"cl":3,"cr":9,"id":"Zqxe7AJ5kXGqSM:","isu":"ru.wikipedia.org","itg":0,"ity":"jpg","oh":274,"ou":"https://upload.wikimedia.org/wikipedia/commons/d/d9/


#<div jscontroller="Q7Rsec" data-ri="0" class="rg_bx rg_di rg_el ivg-i" data-ved="0ahUKEwid2rmyrYffAhVqoYsKHaT-DakQMwg5KAAwAA"><a jsname="hSRGPd" href="#" target="_blank" jsaction="fire.ivg_o;mouseover:str.hmov;mouseout:str.hmou" class="rg_l" rel="noopener"><div class="THL2l"></div><img class="rg_ic rg_i" id="Zqxe7AJ5kXGqSM:" jsaction="load:str.tbn" alt="Картинки по запросу Nelson Mandela" onload="typeof google==='object'&&google.aft&&google.aft(this)"><div class="rg_ilmbg"> 219&nbsp;&#215;&nbsp;274  </div></a><a class="iKjWAf a-no-hover-decoration irc-nic isr-rtc" href="#" jsaction="mouseover:m8Yy5c;mousedown:QEDpme;focus:QEDpme;" rel="noopener" target="_blank"><div class="mVDMnf nJGrxf">Мандела, Нельсон — Википедия</div><div class="nJGrxf FnqxG">ru.wikipedia.org</div></a><div class="rg_meta notranslate">{"cb":21,"cl":3,"cr":9,"id":"Zqxe7AJ5kXGqSM:","isu":"ru.wikipedia.org","itg":0,"ity":"jpg","oh":274,"ou":"https://upload.wikimedia.org/wikipedia/commons/d/d9/Nelson_Mandela-2008_%28edit%29_%28cropped%29.jpg","ow":219,"pt":"Мандела, Нельсон \u2014 Википедия","rh":"ru.wikipedia.org","rid":"buPFJb3ZyATfGM","rt":0,"ru":"https://ru.wikipedia.org/wiki/%D0%9C%D0%B0%D0%BD%D0%B4%D0%B5%D0%BB%D0%B0,_%D0%9D%D0%B5%D0%BB%D1%8C%D1%81%D0%BE%D0%BD","s":"Нельсон Холилала Мандела","sc":1,"st":"Википедия","th":251,"tu":"https://encrypted-tbn0.gstatic.com/images?q\u003dtbn:ANd9GcTvirmz9t9M9TRo-exNTg0b22eX6T7dJa4odoclNZxdVlXcWp6XIg","tw":201}</div></div><!--n--><!--m-->