#!/usr/bin/env python3
import argparse
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.tools.get_difference import get_difference
from gendiff.tools.get_data import get_data


def generate_diff(reference_data, current_data, formatter=stylish):
    data = get_difference(reference_data, current_data, [])
    return formatter(data)


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('-f', '--format', help='set format of output')
    parser.add_argument('reference_file', help='reference file')
    parser.add_argument('current_file', help='current file')
    args = parser.parse_args()
    reference_data = get_data(args.reference_file)
    current_data = get_data(args.current_file)
    res = generate_diff(reference_data, current_data)
    print(res)


if __name__ == '__main__':
    main()
