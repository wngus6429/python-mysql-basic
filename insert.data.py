import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', password='6429', db='blog_db', charset='utf8')
pythonfullstack = db.cursor()
user_email = 'test@test.com'
blog_id = 'A'
sql = "INSERT INTO user_info (USER_EMAIL, BLOG_ID) VALUES ('%s', '%s')" % (str(user_email), str(blog_id))
pythonfullstack.execute(sql)
db.commit()
db.close()