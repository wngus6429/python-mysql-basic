import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', password='6429', db='blog_db', charset='utf8')
pythonfullstack = db.cursor()
sql = "SELECT * FROM user_info"
pythonfullstack.execute(sql)
results = pythonfullstack.fetchall()
for result in results:
    print (result, type(result))
db.commit()
db.close()