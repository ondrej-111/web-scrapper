from lxml.html import fromstring
import requests
from flask import abort
from .Config import Config


def google_search(search_input, proxy):
    return requests.get('https://www.google.com/search', params={'q': search_input}, proxies=proxy)


def google_search_crawlera(search_input):
    return requests.get('https://www.google.com/search', params={'q': search_input}, proxies={
        'http': Config.get('DEFAULT', 'crawlera_url')
    })


def get_first_result(html):
    parser = fromstring(html)

    aes = parser.xpath('//body/div/div/div/div/a[1]')
    if len(aes) > 0:
        sub_a = aes[1].attrib['href'][len('/url?q='):]
        return sub_a[:sub_a.find('&sa=U')]
    else:
        abort(409, 'No results containing all your search terms were found.')

