import scrapy


from scrapy.item import Item, Field
from scrapy.http import FormRequest
from scrapy.spider import Spider
from scrapy.utils.response import open_in_browser


class QuotesSpider(scrapy.Spider):
    name = "mark"
    start_urls = ['http://exam.cusat.ac.in/erp5/cusat/CUSAT-RESULT/latest_uni_result/rresult1']

    def parse(self, response):
        formdata = {'regno': 'C5B'}
        yield FormRequest.from_response(response,
                                        formdata=formdata,
                                        clickdata={'id': 'regcrawl1'},
                                        callback=self.parse1)

    def parse1(self, response):
        open_in_browser(response)

    #def parse(self, response):
    #    page = response.url.split("/")[-2]
     #   filename = 'quotes-%s.html' % page
     #   with open(filename, 'wb') as f:
     #       f.write(response.body)
