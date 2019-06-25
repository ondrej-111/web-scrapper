import requests
from lxml.html import fromstring
import os
from helpers import create_csv, write_to_csv
import json


class ProxyScrapper:
    PROXY_HEADER = ('ip', 'port', 'https', 'valid')

    def __init__(self, config):
        self.config = config
        self.csv_path = config.get('PROXY_SCRAPPER', 'csv_proxies')

    def get_proxies_from_free_proxy(self):

        response = requests.get(self.config.get('PROXY_SCRAPPER', 'free_proxy'))
        parser = fromstring(response.text)
        proxies = set()
        for i in parser.xpath('//tbody/tr'):
            if i.xpath('.//td[7][contains(text(),"yes")]'):
                # Grabbing IP and corresponding PORT
                proxy = ":".join(
                    [i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0], i.xpath('.//td[7]/text()')[0]])
                proxies.add(tuple(proxy.split(':')))
        return proxies

    def get_proxies_from_proxy_docker(self):

        response = requests.get(self.config.get('PROXY_SCRAPPER', 'proxy_docker'))
        parser = fromstring(response.text)
        token = parser.xpath("//meta[@name='_token']")[0].attrib['content']
        response = requests.get(self.config.get('PROXY_SCRAPPER', 'proxy_docker') + '/en/api/proxylist/',
                                params={'token': token, 'country': 'all', 'city': 'all', 'state': 'all',
                                        'port': 'all', 'type': 'all', 'anonymity': 'all', 'need': 'Google', 'page': 1})
        result = json.loads(response.text)
        return result['proxies']

    def test_proxy_in_google(self):
        pass

    def create_csv(self):
        if os.path.isfile(self.csv_path):
            os.remove(self.csv_path)

        create_csv(self.csv_path, ProxyScrapper.PROXY_HEADER)

    def save_to_csv(self, proxies):
        write_to_csv(self.csv_path, proxies)

    def proxy_builder(self, proxies, index):
        proxy = {}
        if proxies['https'][index] == 'yes':
            proxy['https'] = '%s:%s' % (proxies['ip'][index], proxies['port'][index])
        return proxy
