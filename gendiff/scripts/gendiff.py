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


def generate_diff(data1, data2):    
    reference_data = sorted({**data1, **data2})
    diff_list = []
    for key in reference_data:
        value1 = data1.get(key, None)
        value2 = data2.get(key, None)
        if value1 == value2:
            diff_list.append(get_diff_string('no diff', key, value1))
        elif value1 is None:
            diff_list.append(get_diff_string('in second', key, value2))
        elif value2 is None:
            diff_list.append(get_diff_string('in first', key, value1))
        else:
            diff_list.append(get_diff_string('in first', key, value1))
            diff_list.append(get_diff_string('in second', key, value2))    
    return '{\n' + '\n'.join(diff_list) + '\n}'


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('-f', '--format', help='set format of output')
    parser.add_argument('first_file', help='first_file')
    parser.add_argument('second_file', help='second_file')
    args = parser.parse_args()
    data1 = get_data_from_json(args.first_file)
    data2 = get_data_from_json(args.second_file)    
    res = generate_diff(data1, data2)
    print(res)


if __name__ == '__main__':
    main()
