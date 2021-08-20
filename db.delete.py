import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', password='6429', db='ecommerce', charset='utf8')
ecommerce = db.cursor()
sql = """DELETE FROM product WHERE PRODUCT_CODE='2145345'"""
ecommerce.execute(sql)
db.commit()
db.close()