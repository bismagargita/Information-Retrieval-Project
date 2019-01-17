import scrapy
import re
import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'bisma',
    passwd = '123',
    database = 'scraps'
)
mycursor = db.cursor()
query = 'INSERT INTO produk (id_barang,judul,harga,link,link_img,id_ecmr) values (%s,%s,%s,%s,%s,%s)'

class elevenia(scrapy.Spider):
    name = 'elevenia'
    start_urls = ['http://www.elevenia.co.id/ctg-handphone-lainnya']

    def parse(self, response):
        for x in response.css('ul.prodListType > ul.revampList > li.itemList > div.group'):
            '''yield{
                'judul': x.css('a.pordLink::text').extract_first(),
                'harga': ''.join(x.css('div.price > div.prc > strong::text').re(r'[\d]*')),
                'link': x.css('a.img::attr(href)').extract_first(),
                'link_gambar': x.css('a.img > img::attr(src)').extract_first(),
                'id': x.css('a.img::attr(href)').re(r'.*?([0-9]+)$'),
                }'''
            
            judul = x.css('a.pordLink::text').extract_first()
            harga = ''.join(x.css('div.price > div.prc > strong::text').re(r'[\d]*'))
            link = x.css('a.img::attr(href)').extract_first()
            link_gambar = x.css('a.img > img::attr(src)').extract_first()
            id1 = x.css('a.img::attr(href)').re_first(r'.*?([0-9]+)$')
            id2 = 'e' + id1
            value = (id2,judul,harga,link,link_gambar,'2')
            #print(value)
            mycursor.execute(query,value)

        db.commit()
