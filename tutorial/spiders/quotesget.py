import scrapy
import re


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)

class QuotesSpider2(scrapy.Spider):
    name = "quotessave"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for quote in response.css('div.quote'):
			text = quote.css('span.text::text').extract_first()
			author= quote.css('small.author::text').extract_first()
			tags= quote.css('a.tag::text').extract()
			text = re.sub('[;]', '', text)
			
			            
			
			yield dict(text = text,author= author,tags=tags)
