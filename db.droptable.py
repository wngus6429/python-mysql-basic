import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', password='6429', db='ecommerce', charset='utf8')
ecommerce = db.cursor()
sq1 = """DROP TABLE items""";
sq2 = """DROP TABLE ranking""";
ecommerce.execute(sq1)
ecommerce.execute(sq2)
db.commit()
db.close()