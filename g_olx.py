import scrapy
import re
import mysql.connector
#import storage

#mycursor = storage.connect()
db = mysql.connector.connect(
    host = 'localhost',
    user = 'bisma',
    passwd = '123',
    database = 'scraps'
)
mycursor = db.cursor()
query = 'INSERT INTO produk (id_barang,judul,harga,link,link_img,id_ecmr) values (%s,%s,%s,%s,%s,%s)'

class olx(scrapy.Spider):
    name = 'olx'
    start_urls = ['https://www.olx.co.id/elektronik-gadget/handphone/malang-kota/']

    def parse(self, response):
        for x in response.css('ul#gallerywide > li.clickable-div'):
            '''yield{
                'judul': x.css('div.brkword > div.clr > h4.normal > a::attr(title)').extract_first(),
                'harga': ''.join(x.css('div.brkword > div.clr > p.price > strong::text').re(r'[\d]*')),
                'link': x.css('div.brkword > div.clr > h4.normal > a::attr(href)').extract_first(),
                'link_gambar': x.css('div.tcenter > a > img::attr(src)').extract_first(),
                'id': x.css('.package-container button.phone::attr(data-ad-id-temp)').extract_first(),
                }'''
            
            judul = x.css('div.brkword > div.clr > h4.normal > a::attr(title)').extract_first()
            harga = ''.join(x.css('div.brkword > div.clr > p.price > strong::text').re(r'[\d]*'))
            link = x.css('div.brkword > div.clr > h4.normal > a::attr(href)').extract_first()
            link_gambar = x.css('div.tcenter > a > img::attr(src)').extract_first()
            id1 = x.css('.package-container button.phone::attr(data-ad-id-temp)').extract_first()
            id2 = 'o' + id1
            value = (id2,judul,harga,link,link_gambar,'1')
            #print(value)
            mycursor.execute(query,value)

        for href in response.css('div.pager > span.fbold > a::attr(href)'):
            url = href.extract()
            yield scrapy.Request(url, self.parse)

        db.commit()
