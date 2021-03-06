import scrapy
import re

class olx(scrapy.Spider):
	name = 'olx'
	start_urls = ['https://www.olx.co.id/elektronik-gadget/handphone/lg/malang-kota/']
	f = open('hasil.txt', 'w')

	def parse_item(self, response):

		for x in response.css('.offerbody'):
			yield{
				'judul': x.css('.offerheadinner h1.brkword::text').re_first(r'\w+ .*[^\\t\\r\\n\s*]'),
				'harga': x.css('strong.xxxx-large span::text').extract_first(),
				'deskripsi': x.css('#textContent span::text').re(r'[\w]*[^\W]'),
				'id': x.css('.nowrap span.inlblk::text').re_first(r'.+[^\\t\s]'),
			}
			judul = x.css('.offerheadinner h1.brkword::text').re_first(r'\w+ .*[^\\t\\r\\n\s*]')
			harga = x.css('strong.xxxx-large span::text').extract_first()
			f = open('hasil.txt', 'a')
			f.write(harga + '\t: ' + judul + '\n')

	def parse(self, response):
		for href in response.css('.clr h4.normal a::attr(href)'):
			url = href.extract()
			yield scrapy.Request(url, self.parse_item)

		for href in response.css('div.clr span.inline-block a::attr(href)'):
			url = href.extract()
			yield scrapy.Request(url, self.parse)
