from lxml.html import fromstring
import requests
from flask import abort
from base.helpers import read_csv
from base.Config import Config
import random


def google_search(search_input, proxy):
    return requests.get('https://www.google.com/search', params={'q': search_input}, proxies=proxy)


def get_first_result(html):
    parser = fromstring(html)

    aes = parser.xpath('//body/div/div/div/div/a[1]')
    if len(aes) > 0:
        sub_a = aes[1].attrib['href'][len('/url?q='):]
        return sub_a[:sub_a.find('&sa=U')]
    else:
        abort(409, 'No results containing all your search terms were found.')


def get_random_proxy():
    proxies = read_csv(Config.get('PROXY_SCRAPPER', 'csv_proxies'))
    index = random.randint(0, len(proxies['ip']) - 1)
    if proxies['type'][index] == 'http':
        return {
            'http': '%s:%s' % (proxies['ip'][index], proxies['port'][index])
        }
    return {
        'https': '%s:%s' % (proxies['ip'][index], proxies['port'][index])
    }
