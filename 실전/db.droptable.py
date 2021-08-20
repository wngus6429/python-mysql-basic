import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', password='6429', db='bestproducts', charset='utf8')
bestproducts = db.cursor()
sq1 = "DELETE FROM ranking"
sq2 = "DELETE FROM items"
bestproducts.execute(sq1)
bestproducts.execute(sq2)
db.commit()
db.close()

