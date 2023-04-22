import argparse
import json
import yaml


def get_data_from_json(file_path):
    with open(file_path) as file:
        data = json.load(file)
    return data


def get_data_from_yaml(file_path):
    with open(file_path) as file:
        data = yaml.safe_load(file)
    return data


def get_data(file_path):
    if file_path.endswith('.json'):
        return get_data_from_json(file_path)
    elif file_path.endswith(('yml', 'yaml')):
        return get_data_from_yaml(file_path)
    else:
        return None


def get_diff_string(diff_status, key, value):
    status = {'no diff': ' ',
              'in first': '-',
              'in second': '+'}
    return f'  {status[diff_status]} {key}: {value}'


def generate_diff(data1, data2):
    keys = sorted(data1.keys() | data2.keys())
    diff_list = []
    for key in keys:
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
    diff_string = '\n'.join(diff_list)
    return f"{{\n{diff_string}\n}}"


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('-f', '--format', help='set format of output')
    parser.add_argument('first_file', help='first_file')
    parser.add_argument('second_file', help='second_file')
    args = parser.parse_args()
    data1 = get_data(args.first_file)
    data2 = get_data(args.second_file)
    res = generate_diff(data1, data2)
    print(res)


if __name__ == '__main__':
    main()
