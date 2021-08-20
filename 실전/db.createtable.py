import pymysql
db = pymysql.connect(host='localhost', port=3306, user='root', password='6429', db='bestproducts', charset='utf8')
bestproducts = db.cursor()
sql = '''
CREATE TABLE items (
    item_code VARCHAR(20) NOT NULL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    ori_price INT NOT NULL,
    dis_price INT NOT NULL,
    discount_percent INT NOT NULL,
    provider VARCHAR(100)
);
'''
#! item 먼저 안하면 ranking 만들때 Foreign key 관련해서 테이블 없다고 에러가 뜸.
sq2 = '''
CREATE TABLE ranking (
    num INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    main_category VARCHAR(50) NOT NULL,
    sub_category VARCHAR(50) NOT NULL,
    item_ranking TINYINT UNSIGNED NOT NULL,
    item_code VARCHAR(20) NOT NULL,
    FOREIGN KEY (item_code) REFERENCES items(item_code)
);
'''
bestproducts.execute(sql)
bestproducts.execute(sq2)
db.commit()
db.close()