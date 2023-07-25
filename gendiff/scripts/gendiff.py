#!/usr/bin/env python3
import argparse
from gendiff.tools.generator import DEFAULT_FORMATTER
from gendiff.tools.generator import FORMATTERS
from gendiff.tools.generator import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('-f', '--format',
                        dest='format',
                        default=DEFAULT_FORMATTER,
                        choices=FORMATTERS.keys(),
                        help='set format of output')
    parser.add_argument('old_file', help='old file')
    parser.add_argument('new_file', help='new file')
    args = parser.parse_args()
    res = generate_diff(args.old_file, args.new_file, args.format)
    print(res)


if __name__ == '__main__':
    main()
