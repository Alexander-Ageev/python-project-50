#!/usr/bin/env python3
import argparse
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.tools.get_difference import get_difference
from gendiff.tools.get_data import get_data


def generate_diff(old_data, new_data, format='stylish'):
    if format == 'plain':
        formatter = plain
    else:
        formatter = stylish
    data = get_difference(old_data, new_data, [])
    return formatter(data)


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('-f', '--format', dest='format', default='stylish',
                        help='set format of output')
    parser.add_argument('old_file', help='old file')
    parser.add_argument('new_file', help='new file')
    args = parser.parse_args()
    old_data = get_data(args.old_file)
    new_data = get_data(args.new_file)
    res = generate_diff(old_data, new_data, args.format)
    print(res)


if __name__ == '__main__':
    main()
