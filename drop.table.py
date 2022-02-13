import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', password='6429', db='blog_db', charset='utf8')
pythonfullstack = db.cursor()
sql = "drop table user_info"
pythonfullstack.execute(sql)
db.commit()
db.close()