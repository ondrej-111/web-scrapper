import requests
from flask import abort, make_response, jsonify
from .Config import Config
from bs4 import BeautifulSoup

USER_AGENT = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}


def get_bool(bool_value):
    if bool_value in ['True', 'true', 1]:
        return True
    return False


def google_search(search_input, proxy):
    return requests.get('https://www.google.com/search', params={'q': search_input}, proxies=proxy)


def google_search_crawlera(search_input):
    return requests.get('https://www.google.com/search', headers=USER_AGENT, params={'q': search_input}, proxies={
        'http': 'http://{}'.format(Config.get('DEFAULT', 'crawlera_uri'))
    })


def get_first_result(html):
    soup = BeautifulSoup(html, 'html.parser')

    try:
        link = None
        result_block = soup.find_all('div', attrs={'class': 'g'})
        for result in result_block:
            link = result.find('a', href=True)
            break
        return link['href']
    except IndexError:
        abort(make_response(jsonify(message='No results founds.'), 409))
