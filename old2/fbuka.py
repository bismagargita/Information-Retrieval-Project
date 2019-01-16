import scrapy
import re

class bukalapak(scrapy.Spider):
	name = 'bukalapak'
	start_urls = ['https://www.bukalapak.com/c/handphone']
	f = open('link.txt', 'w')

	def parse_item(self, response):
		for x in response.css('div.c-panel__body'):
                        judul = x.css('h1.c-product-detail__name::text').extract_first()
			harga = x.css('div.c-product-detail-price span.amount::text').extract_first()
			yield{
				'judul': judul,
				'harga': harga
			}
			#f = open('hasil.txt', 'a')
			#f.write(harga + '\t: ' + judul + '\n')

	def parse(self, response):
		for href in response.css('div.product-description>h3 a::attr(href)'):
			url = href.extract()
			f = open('link.txt', 'a')
			f.write('https://www.bukalapak.com' + url + '\n\n')
			#yield{'url': url}
			yield response.follow(url, self.parse_item)


		"""for href in response.css('div.clr span.inline-block a::attr(href)'):
			url = href.extract()
			yield scrapy.Request(url, self.parse)"""
