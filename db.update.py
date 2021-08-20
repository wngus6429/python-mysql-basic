import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', password='6429', db='ecommerce', charset='utf8')
ecommerce = db.cursor()
sql = """
    UPDATE product SET
    TITLE='홀복이 짱이지 무슨',
    ORI_PRICE=50000, 
    DISCOUNT_PRICE=25000, 
    DISCOUNT_PERCENT=50
    WHERE PRODUCT_CODE='215673141'
    """
ecommerce.execute(sql)
db.commit()
db.close()

