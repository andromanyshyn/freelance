import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://www.vidal.ru/drugs/molecules'


def get_soup(url):
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    return soup


def get_data(url):
    last_page = int(get_soup(url).find('span', 'last').find('a')['href'].split('p=')[1])

    for i in range(1, last_page + 1):
        if i == 1:
            table = get_soup(url).find('table', 'products-table').find_all('a')
            elements = [line.text for line in table]

            zip_words = zip(
                [line for line in elements[::3]],
                [line for line in elements[1::3]]
            )

            with open('vidal.csv', 'w', encoding='utf-8') as file:
                writer = csv.writer(file, delimiter='|')
                writer.writerow(['Название русское', 'Название на латыни'])
                for line in list(zip_words):
                    writer.writerow(line)
        else:
            url = f'https://www.vidal.ru/drugs/molecules?p={i}'
            table = get_soup(url).find('table', 'products-table').find_all('a')
            elements = [line.text for line in table]

            zip_words = zip(
                [line for line in elements[::3]],
                [line for line in elements[1::3]]
            )

            with open('vidal.csv', 'a', encoding='utf-8') as file:
                writer = csv.writer(file, delimiter='|')
                for line in list(zip_words):
                    writer.writerow(line)


def main():
    get_soup(URL)
    get_data(URL)


if __name__ == '__main__':
    main()
