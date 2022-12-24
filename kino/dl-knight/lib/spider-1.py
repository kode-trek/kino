import scrapy

class _spider(scrapy.Spider):
 name = "dl-link"
 start_urls = ['http://127.0.0.1/']
 def parse(self, response):
  for i in response.css('a'):
   yield {
    'text': i.css('a::text').getall(),
    'href': i.css('a::attr(href)').getall(),
   }
