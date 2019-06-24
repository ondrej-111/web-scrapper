from helpers import get_config, parse_input_args, read_csv, write_row_csv, google_search, proxy_builder

args = parse_input_args()
config = get_config(args)

proxy_csv = config.get('PROXY_SCRAPPER', 'csv_proxies')

proxies = read_csv(proxy_csv)

proxies_count = range(0, len(proxies['ip']))
for i in proxies_count:
    is_valid = True
    try:
        response = google_search('test', proxy_builder(proxies, i))

        if i % 10:
            print('Proccessed: %s/%s\n' % (str(i), str(proxies_count)))

        if response.status_code != 200:
            raise Exception('Not valid proxy')
    except Exception as e:
        is_valid = False

    write_row_csv(proxy_csv, i, 'valid', str(is_valid))
    i += 1

print('Proccessed: %s/%s\n' % (str(proxies_count), str(proxies_count)))
print('Verification finished\n')
