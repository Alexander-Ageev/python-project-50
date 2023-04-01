import argparse
import json


def get_data_from_json(file_path):
    with open(file_path) as file:
        data = json.load(file)
    return data


def get_diff_string(diff_status, key, value):
    status = {'no diff': ' ',
              'in first': '-',
              'in second': '+'}
    return f'  {status[diff_status]} {key}: {value}'


def generate_diff(file_path1, file_path2):
    data1 = get_data_from_json(file_path1)
    data2 = get_data_from_json(file_path2)
    reference_data = sorted({**data1, **data2})
    diff_list = ['{']
    for key in reference_data:
        value1 = data1.get(key, None)
        value2 = data2.get(key, None)
        if value1 == value2:
            diff_list.append(get_diff_string('no diff', key, data1[key]))
        elif value1 is None:
            diff_list.append(get_diff_string('in second', key, data2[key]))
        elif value2 is None:
            diff_list.append(get_diff_string('in first', key, data1[key]))
        else:
            diff_list.append(get_diff_string('in first', key, data1[key]))
            diff_list.append(get_diff_string('in second', key, data2[key]))
    diff_list.append('}')
    return '\n'.join(diff_list)


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('-f', '--format', help='set format of output')
    parser.add_argument('first_file', help='first_file')
    parser.add_argument('second_file', help='second_file')
    args = parser.parse_args()
    res = generate_diff(args.first_file, args.second_file)
    print(res)


if __name__ == '__main__':
    main()
