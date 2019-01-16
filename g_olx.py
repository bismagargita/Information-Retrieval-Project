import scrapy
import re

class olx(scrapy.Spider):
    name = 'olx'
    start_urls = ['https://www.olx.co.id/elektronik-gadget/handphone/malang-kota/']

    def parse(self, response):
        for x in response.css('ul.gallerywide > li.clickable-div'):
            yield{
                'judul': x.css('div.brkword > div.clr > h4.normal > a::attr(title)').extract_first(),
                'harga': ''.join(x.css('div.brkword > div.clr > p.price > strong::text').re(r'[\d]*')),
                'link': x.css('div.brkword > div.clr > h4.normal > a::attr(href)').extract_first(),
                'link_gambar': x.css('div.tcenter > a > img::attr(src)').extract_first(),
                'id': x.css('.package-container button.phone::attr(data-ad-id-temp)').extract_first(),
                }
