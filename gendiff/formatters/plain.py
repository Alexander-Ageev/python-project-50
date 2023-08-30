"""
Модуль реализует форматтер plain для модуля gendiff.
Позволяет выводить данные об изменениях параметров в виде "плоской"
структуры с соответствующими статусами:
Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
"""


from gendiff.tools import (ADDED, REMOVED, UPDATED, NESTED)
import json


def get_correct_value(value):
    """Функция преобразует вывод значений в заданном формате"""
    if isinstance(value, dict):
        result = '[complex value]'
    elif isinstance(value, str):
        result = f'\'{value}\''
    else:
        result = json.dumps(value)
    return result


def make_plain(data, path=''):
    """
    Функция реализует форматтер plain. На вход получает данные об изменениях
    по каждому параметру. Выводит строку соответствующего формата
    """
    plain_data = []
    for record in data:
        key = record['key']
        value = record['value']
        status = record['status']
        current_path = '.'.join([path, key]) if path != '' else key
        status_string = f'Property \'{current_path}\' was {status}'
        if status == NESTED:
            plain_data.append(make_plain(value, current_path))
        elif status == ADDED:
            line = f'{status_string} with value: {get_correct_value(value)}'
            plain_data.append(line)
        elif status == REMOVED:
            plain_data.append(status_string)
        elif status == UPDATED:
            old_value = get_correct_value(value[0])
            new_value = get_correct_value(value[1])
            line = f'{status_string}. From {old_value} to {new_value}'
            plain_data.append(line)
    res = '\n'.join(plain_data)
    return res
