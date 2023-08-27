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


from gendiff.tools import (ADDED, EQUAL, REMOVED, UPDATED, NESTED)


BLOCK_OPEN = '{'
BLOCK_CLOSE = '}'
CLOSE = 'close'
DEFAULT_STYLE = {
    'indent': '    ',
    ADDED: '  + ',
    EQUAL: '    ',
    REMOVED: '  - ',
    BLOCK_OPEN: '{',
    BLOCK_CLOSE: '}',
    True: 'true',
    False: 'false',
    None: 'null'
}


def get_children(source_key, source_value, level, status):
    """
    Функция возвращает список всех вложенных параметров с
    учетом уровня вложенности и символов открытия/закрытия блока
    """
    diff = []
    if not isinstance(source_value, dict):
        record = {
            'key': source_key,
            'status': status,
            'level': level,
            'value': source_value
        }
    else:
        keys = sorted(source_value.keys())
        record = {
            'key': source_key,
            'status': status,
            'level': level,
            'value': BLOCK_OPEN
        }
        diff.append(record)
        for key in keys:
            record = get_children(key, source_value[key], level + 1, EQUAL)
            diff.extend(record)
        record = {
            'key': '',
            'status': CLOSE,
            'level': level,
            'value': BLOCK_CLOSE
        }
    diff.append(record)
    return diff


def get_plain_diff(nodes, level):
    """
    Функция преобразует внутренний формат к блочному представлению данных:
    1. Выделяет вложенные структуры символами начала и конца блока,
    2 .Считает уровень вложенности,
    3. Раскрывает вложенные параметры, которые остались не тронутыми
        в результате вычисления различий (со статусами ADDED, REMOVED, NESTED)
    """
    result = []
    for node in nodes:
        diff = []
        key = node['key']
        status = node['status']
        value = node['value']
        if status in {ADDED, REMOVED, EQUAL}:
            diff = get_children(key, value, level, status)
            result.extend(diff)
        elif status == UPDATED:
            diff = get_children(key, value[0], level, REMOVED)
            result.extend(diff)
            diff = get_children(key, value[1], level, ADDED)
            result.extend(diff)
        elif status == NESTED:
            result.append(
                {'key': key,
                 'status': EQUAL,
                 'level': level,
                 'value': BLOCK_OPEN}
            )
            diff = get_plain_diff(value, level + 1)
            result.extend(diff)
            result.append(
                {'key': '',
                 'status': CLOSE,
                 'level': level,
                 'value': BLOCK_CLOSE}
            )
    return result


def format_record(record, style=DEFAULT_STYLE):
    """
    Функция форматирует плоскую структуру отличий
    в соответствии с заданным стилем style.
    """
    indent = style['indent']
    level = record['level']
    status = record['status']
    key = record['key']
    value = style.get(record['value'], record['value'])
    if record['status'] != CLOSE:
        formated_record = f"{indent*level}{style[status]}{key}: {value}"
    else:
        formated_record = f"{indent*level}{style[EQUAL]}{value}"
    return formated_record


def make_stylish(roots, style=DEFAULT_STYLE):
    output = get_plain_diff(roots, 0)
    lines = [format_record(record, style) for record in output]
    return '\n'.join([style[BLOCK_OPEN]] + lines + [style[BLOCK_CLOSE]])
