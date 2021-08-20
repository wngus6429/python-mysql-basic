import requests
from bs4 import BeautifulSoup

res = requests.get('http://corners.gmarket.co.kr/Bestsellers')
soup = BeautifulSoup(res.content, 'html.parser')

def get_category(category_link, category_name):
    print (category_link, category_name)
    res = requests.get(category_link)
    soup = BeautifulSoup(res.content, 'html.parser')
    
    sub_categories = soup.select('div.navi.group ul li a')
    for sub_category in sub_categories:
        print (category_link, category_name, sub_category.get_text(), 'http://corners.gmarket.co.kr/' + sub_category['href'])

categories = soup.select('div.gbest-cate ul.by-group li a')
for category in categories:
    get_category('http://corners.gmarket.co.kr/' + category['href'], category.get_text())

