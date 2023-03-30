import requests
from bs4 import BeautifulSoup
import csv


def get_url():
    for i in range(1, 44):
        if i == 1:
            url = 'https://www.vidal.ru/drugs/molecules'
            response = requests.get(url=url)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'lxml')
            table = soup.find('table', 'products-table').find_all('a')
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
            response = requests.get(url=url)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'lxml')
            table = soup.find('table', 'products-table').find_all('a')
            elements = [line.text for line in table]

            zip_words = zip(
                [line for line in elements[::3]],
                [line for line in elements[1::3]]
            )

            with open('vidal.csv', 'a', encoding='utf-8') as file:
                writer = csv.writer(file, delimiter='|')
                for line in list(zip_words):
                    writer.writerow(line)


get_url()
