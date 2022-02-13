import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', password='6429', db='blog_db', charset='utf8')
pythonfullstack = db.cursor()
sql = """
    CREATE TABLE user_info (
    USER_ID INT UNSIGNED NOT NULL AUTO_INCREMENT,
    USER_EMAIL VARCHAR(100) NOT NULL,
    BLOG_ID CHAR(4),
    PRIMARY KEY(USER_ID)
);
"""
pythonfullstack.execute(sql)
db.commit()
db.close()