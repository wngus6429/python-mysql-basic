import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', password='6429', db='ecommerce', charset='utf8')
mydb = db.cursor()
sql = """CREATE DATABASE blog_db DEFAULT CHARSET=utf8 COLLATE=utf8_bin"""
mydb.execute(sql)
db.commit()
db.close()