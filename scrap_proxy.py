import requests
from lxml.html import fromstring
import os
from helpers import get_config, parse_input_args, create_csv, write_to_csv

args = parse_input_args()
config = get_config(args)


def get_proxies(url):

    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr'):
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            #Grabbing IP and corresponding PORT
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0], i.xpath('.//td[7]/text()')[0]])
            proxies.add(tuple(proxy.split(':')))
    return proxies


proxy_header = ('ip', 'port', 'https', 'valid')
proxies = get_proxies(config.get('PROXY_SCRAPPER', 'url_1'))
proxies_file_path = config.get('PROXY_SCRAPPER', 'csv_proxies')

if os.path.isfile(proxies_file_path) is False:
    create_csv(proxies_file_path, proxy_header)
    write_to_csv(proxies_file_path, proxies)


print('Scraping proxies finished.')
