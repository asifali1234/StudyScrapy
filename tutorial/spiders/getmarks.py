import scrapy


from scrapy.item import Item, Field
from scrapy.http import FormRequest
from scrapy.spider import Spider
from scrapy.utils.response import open_in_browser


class QuotesSpider(scrapy.Spider):
    name = "marks"
    start_urls = ['http://www-mec.mec.ac.in/sessional-marks']

    def parse(self, response):
        formdata = {'class': 'C5B','rollno': '12'}
        yield FormRequest.from_response(response,
                                        formdata=formdata,
                                        clickdata={'name': 'Button1'},
                                        callback=self.parse1)

    def parse1(self, response):
        open_in_browser(response)

    #def parse(self, response):
    #    page = response.url.split("/")[-2]
     #   filename = 'quotes-%s.html' % page
     #   with open(filename, 'wb') as f:
     #       f.write(response.body)
