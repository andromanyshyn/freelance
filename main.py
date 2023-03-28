from bs4 import BeautifulSoup
import requests

url = 'https://www.olx.pl/'


def get_categories():
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    categories = [link['href'] for link in soup.find('div', 'subcategories-list clr', id='bottom4').find_all('a')]
    return categories


def get_subcategories():
    links = get_categories()
    administration = 'https://www.olx.pl/praca/administracja-biurowa/'
    response = requests.get(url=administration)
    soup = BeautifulSoup(response.text, 'lxml')
    print(soup)


print(get_subcategories())
