import argparse
import configparser
import csv
import requests
import os

def parse_input_args():
    parser = argparse.ArgumentParser(description='Input parameters.')

    parser.add_argument('-e', '--env', type=str, help='Set environment', required=True)
    return vars(parser.parse_args())


def get_config(args):
    config = configparser.ConfigParser()
    config.read('config.%s.ini' % args['env'])
    return config


def create_csv(path, header_list):

    with open(path, 'a', encoding="utf-8") as outcsv:
        writer = csv.writer(outcsv)
        writer.writerow(list(header_list))


def write_to_csv(path, data_list):

    with open(path, 'a', encoding="utf-8") as outcsv:
        writer = csv.writer(outcsv)
        for row in data_list:
            writer.writerow(list(row))


def write_row_csv(path, row_number, key, value):
    init_rn = 0
    result = []
    with open(path) as csv_file:
        reader = csv.DictReader(csv_file, skipinitialspace=True)
        for row in reader:
            if init_rn == row_number:
                row[key] = value
            init_rn += 1
            result.append(row)

    os.remove(path)
    result = [result[0].keys(), *[r.values() for r in result]]
    write_to_csv(path, result)


def read_csv(path):
    with open(path) as csvfile:
        reader = csv.DictReader(csvfile, skipinitialspace=True)
        d = {name: [] for name in reader.fieldnames}
        for row in reader:
            for name in reader.fieldnames:
                d[name].append(row[name])
    return d


def google_search(search_input, proxy):
    return requests.get('https://www.google.com/search', params={'q': search_input}, proxies=proxy)


def proxy_builder(proxies, index):
    proxy = {}
    if proxies['https'][index] == 'yes':
        proxy['https'] = '%s:%s' % (proxies['ip'][index], proxies['port'][index])
    return proxy
