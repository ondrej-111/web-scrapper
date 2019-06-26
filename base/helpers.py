import argparse
import csv
import os
from base.Config import Config


def get_bool(bool_value):
    if bool_value in ['True', 'true', 1]:
        return True
    return False


def parse_input_args():
    parser = argparse.ArgumentParser(description='Input parameters.')

    parser.add_argument('-e', '--env', type=str, help='Set environment', required=True)
    return vars(parser.parse_args())


def get_config(args):
    config = Config(args['env'])
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
