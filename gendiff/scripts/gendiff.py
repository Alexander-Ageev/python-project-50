#!/usr/bin/env python3
import argparse
from gendiff.tools.get_data import get_data


STATUS_ADDED = 'added'  # параметр добавлен в текущий файл
STATUS_EQUAL = 'equal'  # параметры совпадают в обоих файлах
STATUS_PASS = 'pass'  # параметр принадлежит к предыдущему уровню
STATUS_REMOVED = 'removed'  # параметр удален из текущего файла
TYPE_NODE = 'node'
TYPE_LEAF = 'leaf'
NO_VALUE = 'value not presented'
DEFAULT_STYLE = {'indent': '    ',
                 STATUS_ADDED: '  + ',
                 STATUS_EQUAL: '    ',
                 STATUS_REMOVED: '  - ',
                 STATUS_PASS: '    ',
                 'block open': '{',
                 'block close': '}'
                 }


def stylish(data, style):
    stilysh_data = [style['block open']]
    ex_level = -1
    for line in data:
        level = line['level']
        indent = style['indent']
        status = style[line['status']]
        key = line['key']
        value = line['value']
        for i in range(ex_level - level):
            stilysh_data.append(indent * (ex_level - i) + style['block close'])
        if line['type'] == TYPE_NODE:
            value = style['block open']
        stilysh_data.append(f'{indent*level}{status}{key}: {value}')
        ex_level = level
    for i in range(level + 1):
        stilysh_data.append(indent * (level - i) + style['block close'])
    return '\n'.join(stilysh_data)


def get_representation(key, value, level, status=STATUS_PASS):
    if isinstance(value, dict):
        node_type = TYPE_NODE
        value = ''
    else:
        node_type = TYPE_LEAF
    res = {'key': key,
           'value': value,
           'level': level,
           'type': node_type,
           'status': status}
    return res


def get_children(data, level):
    childrens = []
    if not isinstance(data, dict):
        return childrens
    keys = sorted(data.items())
    for key, value in keys:
        if isinstance(value, dict):
            childrens.append(get_representation(key, value, level))
            childrens.extend(get_children(value, level + 1))
        else:
            childrens.append(get_representation(key, value, level))
    return childrens


def get_difference(sorted_keys, ref_data, cur_data, level):
    representation = []
    for key in sorted_keys:
        reference_value = ref_data.get(key, NO_VALUE)
        current_value = cur_data.get(key, NO_VALUE)
        if isinstance(reference_value, dict) and isinstance(current_value, dict):
            representation.append(get_representation(key, reference_value, level))
            new_keys = sorted(reference_value.keys() | current_value.keys())
            representation.extend(get_difference(new_keys, reference_value, current_value, level + 1))
        elif reference_value is NO_VALUE:
            representation.append(get_representation(key, current_value, level, STATUS_ADDED))
            representation.extend(get_children(current_value, level + 1))
        elif current_value is NO_VALUE:
            representation.append(get_representation(key, reference_value, level, STATUS_REMOVED))
            representation.extend(get_children(reference_value, level + 1))
        elif reference_value == current_value:
            representation.append(get_representation(key, reference_value, level, STATUS_EQUAL))
        elif reference_value != current_value:
            representation.append(get_representation(key, reference_value, level, STATUS_REMOVED))
            representation.extend(get_children(reference_value, level + 1))
            representation.append(get_representation(key, current_value, level, STATUS_ADDED))
            representation.extend(get_children(current_value, level + 1))
        else:
            assert True, 'Что-то пошло не по плану :('
    return representation


def generate_diff(reference_data, current_data, style=DEFAULT_STYLE):
    keys = sorted(reference_data.keys() | current_data.keys())
    data = get_difference(keys, reference_data, current_data, 0)
    return stylish(data, style)


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
