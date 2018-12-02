import scrapy
import re

class Lazada(scrapy.Spider):
	name = 'lazada'
	start_urls = ['https://www.lazada.co.id/iphone/']
	f = open('link.txt', 'w')

	"""def parse_item(self, response):
		for x in response.css('div.c-panel__body'):
                        judul = x.css('h1.c-product-detail__name::text').extract_first()
			harga = x.css('div.c-product-detail-price span.amount::text').extract_first()
			yield{
				'judul': judul,
				'harga': harga
			}
			f = open('hasil.txt', 'a')
			f.write(harga + '\t: ' + judul + '\n')"""

	def parse(self, response):
		for href in response.css('div.c16H9d a::attr(href)'):
			url = href.extract()
			#f = open('link.txt', 'a')
			#f.write(url + '\n\n')
			yield{
				#'url': url,
				'href': href,
			}
			#yield response.follow(url, self.parse_item)


		"""for href in response.css('div.clr span.inline-block a::attr(href)'):
			url = href.extract()
			yield scrapy.Request(url, self.parse)"""
