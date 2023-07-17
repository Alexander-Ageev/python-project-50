"""
Модуль реализует форматтер plain для модуля gendiff.
Позволяет вывести внутреннюю структуру данных gendiff.
"""


import json


def make_json(data):
    # Возвращает внутреннюю структуру данных в виде
    # JSON записей
    res = json.dumps(data)
    return res
