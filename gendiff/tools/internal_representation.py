"""Модуль предназначен для анализа изменений в двух наборах данных"""


from gendiff.tools import (ADDED, EQUAL, REMOVED, UPDATED, NESTED)


def compare_data(old_data, new_data, level):  # noqa: C901
    """
    Функция получает на вход два словаря с наборами параметров
    и путь к этим параметрам. Сверяет каждый параметр в этих словарях.
    Результат выводится в виде списка данных о статусах каждого параметра.
    Статусы описаны в файле gendiff/tools/__init__.py
    """
    sorted_keys = sorted(old_data.keys() | new_data.keys())
    diff = []
    for key in sorted_keys:
        if key not in old_data:
            status = ADDED
            value = new_data[key]
        elif key not in new_data:
            status = REMOVED
            value = old_data[key]
        elif isinstance(old_data[key], dict) and isinstance(
                new_data[key], dict):
            status = NESTED
            value = compare_data(old_data[key], new_data[key], level + 1)
        elif old_data[key] == new_data[key]:
            status = EQUAL
            value = new_data[key]
        elif old_data[key] != new_data[key]:
            status = UPDATED
            value = (old_data[key], new_data[key])
        else:
            assert True, 'Что-то пошло не по плану :('
        data = {
            "key": key,
            "status": status,
            "level": level,
            "value": value
        }
        diff.append(data)
    return diff
