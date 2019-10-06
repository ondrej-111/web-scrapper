from helpers import get_config, parse_input_args
from proxy.ProxyScrapper import ProxyScrapper

args = parse_input_args()
config = get_config(args)


prx_scrapper = ProxyScrapper(config)

proxies = prx_scrapper.get_proxies_from_proxy_docker()
prx_scrapper.save_to_csv([proxies[0].keys(), *[p.values() for p in proxies]])

print('Scraping proxies finished.')
