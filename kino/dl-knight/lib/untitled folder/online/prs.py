from os import system as s
from shutil import move

def prs(arg1, arg2):
	p1 = '''import scrapy

class QuotesSpider(scrapy.Spider):
	name = "asset"
	start_urls = ["'''

	p2 = '''"]
	def parse(self, response):
		for l in response.css("'''

	p3 = '''"):
			yield {
			'anchor': l.css('a::attr(href)').getall()
			}'''

	fh = open('src.py', 'w')
	fh.write(p1 + arg1 + p2 + arg2 + p3)
	fh.close()

	try:		move('src.py', 'spider_1/spider_1/spiders/')
	except:	pass
