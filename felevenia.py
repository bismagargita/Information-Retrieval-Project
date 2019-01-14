import scrapy
import re

class elevenia(scrapy.Spider):
    name = 'elevenia'
    start_urls = ['http://www.elevenia.co.id/ctg-kamera-dslr']
    f = open('hasil.txt', 'w')

    def parse_item(self, response):
        for x in response.css('.productContent'):
            yield{
                'judul': x.css('div.titleArea > h1::text').extract_first(),
                'harga': x.css('.priceDisc span.price::text').extract_first(),
                'link_img': x.css('div.targetarea > div > a.cloud-zoom').extract_first(),
            }

    def parse(self, response):
        for href in response.css('li.itemList a.pordLink::attr(href)'):
            url = href.extract()
            #yield {'link':href.extract()}
            yield scrapy.Request(url, self.parse_item)        


