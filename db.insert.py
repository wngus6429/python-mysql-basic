import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', password='6429', db='ecommerce', charset='utf8')
ecommerce = db.cursor()
sql = """INSERT INTO product VALUES(
    '2145345', '스위트바니 여름신상5900원~롱원피스티셔츠/긴팔/반팔', 23000, 6900, 70, 'F');"""
ecommerce.execute(sql)
db.commit()
db.close()