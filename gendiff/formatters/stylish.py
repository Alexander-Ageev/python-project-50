"""
Модуль реализует форматтер stylish для модуля gendiff.
Позволяет выводить информацию о разнице файлов в виде вложенной структуры
со статусами добавлен ("+"), удален ("-") и без изменений (" ")
{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}
"""


from gendiff.tools.internal_representation import get_children
from gendiff.tools import (
    ADDED, EQUAL, PASS, REMOVED,
    UPDATED, NODE, TYPE_NODE,
)


DEFAULT_STYLE = {
    'indent': '    ',
    ADDED: '  + ',
    EQUAL: '    ',
    REMOVED: '  - ',
    PASS: '    ',
    UPDATED: '    ',
    NODE: '    ',
    'block open': '{',
    'block close': '}'
}


def get_correct_value(value):
    """Функция преобразует вывод значений в заданном формате"""
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    else:
        return value


def make_stylish(data, style=DEFAULT_STYLE):  # noqa: C901
    """
    Функция реализует форматтер stylish. На вход получает данные
    об изменениях по каждому параметру. Выводит строку соответствующего формата
    """
    stack = data[::-1]
    stilysh_data = [style['block open']]
    ex_level = -1
    while stack:
        line = stack.pop()
        level = len(line['path'])
        indent = style['indent']
        status = line['status']
        key = line['key']
        path = line['path'] + [key]
        if status == EQUAL:
            value = line['old_value']
            value_type = line['old_value_type']
        elif status == ADDED:
            value = line['new_value']
            value_type = line['new_value_type']
            stack.extend(get_children(value, path))
        elif status == REMOVED:
            value = line['old_value']
            value_type = line['old_value_type']
            stack.extend(get_children(value, path))
        elif status == UPDATED:
            value = line['old_value']
            value_type = line['old_value_type']
            status = REMOVED
            added_line = line.copy()
            added_line['status'] = ADDED
            stack.append(added_line)
            stack.extend(get_children(value, path))
        elif status == PASS:
            value = line['old_value']
            value_type = line['old_value_type']
            stack.extend(get_children(value, path))
        elif status == NODE:
            value = ''
            value_type = TYPE_NODE
        else:
            assert True, 'unknown status'
        status_symbol = style[status]
        value = get_correct_value(value)
        for i in range(ex_level - level):
            stilysh_data.append(indent * (ex_level - i) + style['block close'])
        if value_type == TYPE_NODE:
            value = style['block open']
        stilysh_data.append(f'{indent*level}{status_symbol}{key}: {value}')
        ex_level = level
    for i in range(level + 1):
        stilysh_data.append(indent * (level - i) + style['block close'])
    return '\n'.join(stilysh_data)
