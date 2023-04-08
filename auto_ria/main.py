import requests
import json
from bs4 import BeautifulSoup

HOST = 'https://auto.ria.com'
URL_ROOT = 'https://auto.ria.com/newauto/marka-jeep/'

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}


def get_html(url, params=None):
    response = requests.get(url=url, headers=HEADERS, params=params)
    return response


dict_json = []


def get_content(html):
    soup = BeautifulSoup(html, 'lxml')

    name = [data.text.strip() for data in soup.find_all('span', class_='link')[2:-1]]
    usd_price = [price.text.strip() for price in soup.find_all('span', class_='green bold size22')]
    uah_price = [price.text.strip() for price in soup.find_all('span', class_='size16') if price.text != ' '][3:]
    town = [town.text for town in soup.find_all('span', class_='item region')]
    link = [data['href'] for data in soup.find_all('a', class_='proposition_link')]

    for it_name, it_town, it_usdprice, it_uahprice, it_link in zip(name, town, usd_price, uah_price, link):
        dict_json.append({
            'Title': it_name,
            'Town': it_town,
            'USD price': it_usdprice,
            'UAH price': it_uahprice,
            'Link': HOST + it_link
        })
    return dict_json


def save_data():
    with open('AutoRia.json', 'w', encoding='utf-8-sig') as file:
        json.dump(dict_json, file, indent=4, ensure_ascii=False)


def parse():
    html = get_html(URL_ROOT)
    if html.status_code == 200:
        try:
            get_content(html.text)
        except AttributeError:
            return False


parse()
save_data()
