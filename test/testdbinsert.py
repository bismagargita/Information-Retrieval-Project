import mysql.connector

db = mysql.connector.connect(
	host = 'localhost',
	user = 'enigma',
	passwd = 'mitsaqenigma',
	database = 'scraps'
)

mycursor = db.cursor()

query = 'insert into barang (kode,judul,harga) values (%s,%s,%s)'
value = [
	('499326364','Xiaomi redmi note 4x 4/64','1600000'),
	('499246881','Xiaomi Redmi 6 A','1399000')
]

mycursor.executemany(query,value)
db.commit()
