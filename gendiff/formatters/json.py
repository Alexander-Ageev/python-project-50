"""
Модуль реализует форматтер plain для модуля gendiff.
Позволяет вывести внутреннюю структуру данных gendiff.
"""


import json
from gendiff.tools import (ADDED, REMOVED, UPDATED)


def get_difference_data(data):
    """Функция подготавливает данные для вывода"""
    res = {
        'path': '.'.join(data['path']),
        'key': data['key'],
        'old value': data['old_value'],
        'new value': data['new_value'],
        'status': data['status']
    }
    return res


def make_json(data):
    """Возвращает внутреннюю структуру данных в виде JSON записей"""
    res = []
    for record in data:
        if record['status'] in [ADDED, REMOVED, UPDATED]:
            res.append(get_difference_data(record))
    res = json.dumps(res)
    return res
