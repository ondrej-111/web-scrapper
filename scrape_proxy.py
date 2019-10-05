from base.helpers import get_config, parse_input_args
from scripts.ProxyScrapper import ProxyScrapper

args = parse_input_args()
config = get_config(args)


prx_scrapper = ProxyScrapper(config)

proxies_http = prx_scrapper.get_proxies_from_proxy_docker('http')
for prx in proxies_http:
    prx['type'] = 'http'
proxies_https = prx_scrapper.get_proxies_from_proxy_docker('https')
for prx in proxies_https:
    prx['type'] = 'https'

prx_scrapper.create_csv([proxies_http[0].keys(), *[p.values() for p in proxies_http + proxies_https]])

print('Scraping proxies finished.')
