import configparser
import mysql.connector

config = configparser.ConfigParser()
config.read('config.ini')

def connect():
    db = mysql.connector.connect(
        host = config['mysql']['host'],
        user = config['mysql']['user'],
        passwd = config['mysql']['password'],
        database = config['mysql']['database']
    )
