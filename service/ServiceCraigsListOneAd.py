import os
import re

from bs4 import BeautifulSoup


class ServiceCraigsListOneAd:
    __html_data = None
    one_ad = []

    def __init__(self):
        self.__load_html_data()

    def __load_html_data(self):
        self.__html_data = BeautifulSoup(
            open(os.getcwdb().decode('utf-8') + "\\data\\page.html", 'r', encoding='utf-8'), 'html.parser')

    def find(self):
        for ad in self.__html_data.find_all('li', attrs={'class': 'cl-search-result cl-search-view-mode-gallery'}):
            self.one_ad.append({
                'title': re.sub('\n', ' ', ad.find('a', attrs={'class', 'titlestring'}).get_text()),
                'url': re.sub('\n', ' ', ad.find('a', attrs={'class', 'titlestring'})['href']),
                'price': re.sub('\n', ' ', ad.find('span', attrs={'class', 'priceinfo'}).get_text() if ad.find('span', attrs={'class', 'priceinfo'}) else "N/A"),
                'date': re.sub('\n', ' ', ad.find('div', attrs={'class', 'meta'}).get_text().split('·')[0])
            })
