import requests
from bs4 import BeautifulSoup
from typing import List

def scrape():
    url = 'https://www.ozone.bg/'
    html = requests.get(url=url)
    s = BeautifulSoup(html.content,'html.parser')
    results = s.find(id='cat-20132')
    items = results.find_all('h2',class_='product-ttl')
    prices = results.find_all('span',class_=['cur-price notranslate','cur-price notranslate cur-price-per'])
    item_titles = [(item.text,price.text) for item,price in zip(items,prices)]   
    with open('items.txt','w',encoding='utf-8') as file:
        for item in item_titles:
            file.write(f'Име: {item[0]}, Цена: {item[1]}\n')

def main():
    scrape()

def get_first_n(n:int)->List[str]:
    item_titles = []
    with open('items.txt','r',encoding='utf-8') as file:
        for i in range(0,n):
            item_titles.append(file.readline().strip())
    return item_titles

if __name__ == '__main__':
    main()