import scrapy

class QuotesSpider(scrapy.Spider):
	name = "asset"
	start_urls = ["http://dl.bestsitcom.ir/HIMYM/720/2/"]
	def parse(self, response):
		for l in response.css("body"):
			yield {
			'anchor': l.css('a::attr(href)').getall()
			}