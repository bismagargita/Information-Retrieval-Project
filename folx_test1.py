import scrapy
import re
import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'bisma',
    passwd = '123',
    database = 'scraps'
)

link = "test_link"
mycursor = db.cursor()
query = 'INSERT INTO produk (id_barang,judul,harga,deskripsi,link_img,id_ecmr) values (%s,%s,%s,%s,%s,%s)'

class olx(scrapy.Spider):
    name = 'olx'
    start_urls = ['https://www.olx.co.id/elektronik-gadget/handphone/lg/malang-kota/']
    f = open('hasil.txt', 'w')

    def parse_item(self, response):

        for x in response.css('.offerbody'):
            """
            yield{
                #'judul': x.css('.offerheadinner h1.brkword::text').re_first(r'\w+ .*[^\\t\\r\\n\s*]'),
                #'harga': ''.join(x.css('strong.xxxx-large span::text').re(r'[\w]*')),
                #'deskripsi': ' '.join(x.css('#textContent span::text').re(r'[\w]*[^\W]')),
                #'id': x.css('.nowrap span.inlblk::text').re_first(r'.+[^\\t\s]'),
                'url': link,
                #'img_link': x.css('#bigGallery li.fleft > a::attr(href)').extract_first(),
                
            }
            """

            id_p = x.css('.nowrap span.inlblk::text').re_first(r'.+[^\\t\s]')
            judul1 = x.css('.offerheadinner h1.brkword::text').re_first(r'\w+ .*[^\\t\\r\\n\s*]')
            harga1 = ''.join(x.css('strong.xxxx-large span::text').re(r'[\w]*'))
            deskripsi = ' '.join(x.css('#textContent span::text').re(r'[\w]*[^\W]'))
            link_img = x.css('#bigGallery li.fleft > a::attr(href)').extract_first()
            global link
            link_produk = link
            value = (id_p,judul1,harga1,deskripsi,link_img,link_produk,'1')
            print('judul : ', judul1, 'link produk : ', link_produk)
            #mycursor.execute(query,value)
            

            judul = x.css('.offerheadinner h1.brkword::text').re_first(r'\w+ .*[^\\t\\r\\n\s*]')
            harga = x.css('strong.xxxx-large span::text').extract_first()
            f = open('hasil.txt', 'a')
            f.write(harga + '\t: ' + judul + '\n')

    def parse(self, response):
        for href in response.css('.clr h4.normal a::attr(href)'):
            url = href.extract()
            global link
            link = url
            yield scrapy.Request(url, self.parse_item)

        for href in response.css('div.clr span.inline-block a::attr(href)'):
            url = href.extract()    
            yield scrapy.Request(url, self.parse)
            
        db.commit()

