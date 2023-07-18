"""
Модуль реализует форматтер plain для модуля gendiff.
Позволяет выводить данные об изменениях параметров в виде "плоской"
структуры с соответствующими статусами:
Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
"""


from gendiff.tools import (
    ADDED, EQUAL, PASS, REMOVED,
    UPDATED, NODE,
)


def get_correct_value(value):
    """Функция преобразует вывод значений в заданном формате"""
    if isinstance(value, dict):
        result = '[complex value]'
    elif value is True:
        result = 'true'
    elif value is False:
        result = 'false'
    elif value is None:
        result = 'null'
    elif isinstance(value, str):
        result = f'\'{value}\''
    else:
        result = value
    return result


def make_plain(data):  # noqa: C901
    """
    Функция реализует форматтер plain. На вход получает данные об изменениях
    по каждому параметру. Выводит строку соответствующего формата
    """
    plain_data = []
    for line in data:
        key = line['key']
        path = '.'.join(line['path'] + [key])
        status = line['status']
        status_string = f'Property \'{path}\' was {status}'
        new_line = ''
        if status in [EQUAL, PASS, NODE]:
            pass
        elif status == ADDED:
            new_value = get_correct_value(line['new_value'])
            new_line = f'{status_string} with value: {new_value}'
        elif status == REMOVED:
            new_line = status_string
        elif status == UPDATED:
            old_value = get_correct_value(line['old_value'])
            new_value = get_correct_value(line['new_value'])
            new_line = f'{status_string}. From {old_value} to {new_value}'
        else:
            assert True, 'unknown status'
        if new_line:
            plain_data.append(new_line)
    res = '\n'.join(plain_data)
    return res
