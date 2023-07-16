#!/usr/bin/env python3
import argparse
from jsondiff import diff
from gendiff.formatters.stylish import stylish  # noqa E402
from gendiff.formatters.plain import plain  # noqa E402
from gendiff.tools.get_difference import get_difference  # noqa E402
from gendiff.tools.get_data import get_data  # noqa E402


def generate_diff(old_data, new_data, format='stylish'):
    if format == 'json':
        return diff(old_data, new_data)
    elif format == 'plain':
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
