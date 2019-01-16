import scrapy
import re

class elevenia(scrapy.Spider):
    name = 'elevenia'
    start_urls = ['http://www.elevenia.co.id/ctg-handphone-android']

    def parse(self, response):
        for x in response.css('ul.prodListType > ul.revampList > li.itemList > div.group'):
            yield{
                'judul': x.css('a.pordLink::text').extract_first(),
                'harga': ''.join(x.css('div.price > div.prc > strong::text').re(r'[\d]*')),
                'link': x.css('a.img::attr(href)').extract_first(),
                'link_gambar': x.css('a.img > img::attr(src)').extract_first(),
                'id': x.css('a.img::attr(href)').re(r'.*?([0-9]+)$'),
                }
