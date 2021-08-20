import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', password='6429', db='ecommerce', charset='utf8')
ecommerce = db.cursor()
sql = "SELECT * FROM product;"
ecommerce.execute(sql)
#result = ecommerce.fetchall()
#result = ecommerce.fetchmany(size=4)
result = ecommerce.fetchone()
print(result)
#튜플형태로 저장되니까 주의해야한다.
#for record in result:
#    print(record)
db.commit()
db.close()