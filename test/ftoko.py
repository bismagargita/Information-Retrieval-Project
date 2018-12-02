import scrapy
#import re

class tokopedia(scrapy.Spider):
	name = 'tokopedia'
	start_urls = ['https://www.tokopedia.com/search?q=rtx+2070']
	f = open('link.txt', 'w')

	def parse(self, response):
		for href in response.css('._27sG_y4O a::attr(href)'):
			url = href.extract()
			yield{
				'url': href,
				'href': url,
			}
			f = open('link.txt', 'a')
			f.write(url)
			#yield response.follow(url, self.parse_item)

	"""def parse_item(self, response):
		for x in response.css('div.rvm-left-column--right'):
			judul = x.css('h1.rvm-product-title::text').extract_first()
			harga = x.css('#product_price_int input::attr(value)').extract_first()
			yield{
				'judul': judul,
				'harga': harga,
			}
			f = open('hasil.txt', 'a')
			f.write(harga + '\t: ' + judul + '\n')

		for href in response.css('div.clr span.inline-block a::attr(href)'):
			url = href.extract()
			yield scrapy.Request(url, self.parse)"""
