#!/usr/bin/env python3
import argparse
from gendiff.formatters.stylish import make_stylish  # noqa E402
from gendiff.formatters.json import make_json  # noqa E402
from gendiff.formatters.plain import make_plain  # noqa E402
from gendiff.tools.get_data import get_data  # noqa E402


FORMATTERS = {
    'plain': make_plain,
    'json': make_json,
    'stylish': make_stylish
}


def generate_diff(old_file, new_file, format='stylish'):
    old_data = get_data(old_file)
    new_data = get_data(new_file)
    output = FORMATTERS.get(format, 'stylish')(old_data, new_data)
    return output


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('-f', '--format', dest='format', default='stylish',
                        help='set format of output')
    parser.add_argument('old_file', help='old file')
    parser.add_argument('new_file', help='new file')
    args = parser.parse_args()
    res = generate_diff(args.old_file, args.new_file, args.format)
    print(res)


if __name__ == '__main__':
    main()
