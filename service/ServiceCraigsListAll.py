import re
from time import sleep

import requests as requests
from bs4 import BeautifulSoup


class ServiceCraigsListAll:
    all_ads = []
    headers = []

    def set_more_info(self, ad_info: dict):

        print('It will take a long time ...')

        for element in ad_info:
            result = requests.get(element['url'])
            if result.status_code == 200:
                html_data = BeautifulSoup(result.content.decode('utf-8'), 'html.parser')

                if html_data.find_all('p', attrs={'class': 'attrgroup'}):
                    for additional_info in re.sub('\n', ' ', html_data.find_all('p', attrs={'class': 'attrgroup'})[
                        1].get_text()).split('  '):
                        temp = additional_info.split(':')
                        if len(temp) >= 2:
                            element[temp[0].replace(' ', '_')] = temp[1]

                    keys = list(element.keys())

                    if len(keys) > len(self.headers):
                        self.headers = keys

            self.all_ads.append(element)
            sleep(1)

    def show_info(self):
        # Write csv header
        print(', '.join(self.headers))

        # Write csv content
        for element in self.all_ads:
            print(', '.join(list(element.values())))
