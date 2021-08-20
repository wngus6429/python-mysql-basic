import requests
from bs4 import BeautifulSoup
import pymysql
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='6429', db='bestproducts', charset='utf8')
cursor = db.cursor()

res = requests.get('http://corners.gmarket.co.kr/Bestsellers')
soup = BeautifulSoup(res.content, 'html.parser')

def get_category(category_link, category_name):
    print (category_link, category_name)
    res = requests.get(category_link)
    soup = BeautifulSoup(res.content, 'html.parser')

    get_items(soup, category_name, "ALL")
    
    sub_categories = soup.select('div.navi.group ul li > a')
    for sub_category in sub_categories:
        res = requests.get('http://corners.gmarket.co.kr/' + sub_category['href'])
        soup = BeautifulSoup(res.content, 'html.parser')
        get_items(soup, category_name, sub_category.get_text())
        
def get_items(html, category_name, sub_category_name):
    items_result_list = list()
    best_item = html.select('div.best-list')
    for index, item in enumerate(best_item[1].select('li')):
        data_dict = dict()
        
        ranking = index + 1
        title = item.select_one('a.itemname')
        ori_price = item.select_one('div.o-price')
        dis_price = item.select_one('div.s-price strong span')
        discount_percent = item.select_one('div.s-price em')

        if ori_price == None or ori_price.get_text() == '':
            ori_price = dis_price
        
        if dis_price == None:
            ori_price, dis_price = 0, 0
        else:
            ori_price = ori_price.get_text().replace(',', '').replace('원', '')
            dis_price = dis_price.get_text().replace(',', '').replace('원', '')

        if discount_percent == None or discount_percent.get_text() == '':
            discount_percent = 0
        else:
            discount_percent = discount_percent.get_text().replace('%', '')
        
        product_link = item.select_one('div.thumb > a')
        item_code = product_link.attrs['href'].split('=')[1]
        
        res = requests.get(product_link.attrs['href'])
        soup = BeautifulSoup(res.content, 'html.parser')
        
        # 2021.04.03 : 웹페이지가 변경되어, 다음 provider CSS Selector 수정이 필요합니다
        # 다음 코드와 실제 해당 웹페이지를 비교해보시면서, 영상과의 차이점까지 이해해보시면,
        # 다양한 케이스에서 어떻게 CSS Selector 를 써서, 크롤링을 할 수 있을지 보다 이해하실 수 있을 것 같습니다.
        provider = soup.select_one('div.item-topinfo_headline > p > span > a')
        
        if provider == None:
            provider = ''
        else:
            provider = provider.get_text()
            
        data_dict['category_name'] = category_name
        data_dict['sub_category_name'] = sub_category_name
        data_dict['ranking'] = ranking
        data_dict['title'] = title.get_text()
        data_dict['ori_price'] = ori_price
        data_dict['dis_price'] = dis_price
        data_dict['discount_percent'] = discount_percent
        data_dict['item_code'] = item_code
        data_dict['provider'] = provider        
        
        save_data(data_dict)
        # print (category_name, sub_category_name, ranking, item_code, "PROVIDER:" + provider, "---", title.get_text(), 
        #ori_price, dis_price, discount_percent)    

categories = soup.select('div.gbest-cate ul.by-group li a')
for category in categories:
    get_category('http://corners.gmarket.co.kr/' + category['href'], category.get_text())


