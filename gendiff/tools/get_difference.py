"""
Модуль предназначен для анализа изменений в двух наборах данных
"""


from gendiff.tools import (
    ADDED, EQUAL, PASS, REMOVED,
    UPDATED, NODE, TYPE_NODE, TYPE_LEAF
)


def get_compare_status(path, key, old_value, new_value=None, status=PASS):
    """
    Функция записывает результат сравнения двух параметров в виде словаря.
    """
    if isinstance(old_value, dict):
        old_value_type = TYPE_NODE
    else:
        old_value_type = TYPE_LEAF
    if isinstance(new_value, dict):
        new_value_type = TYPE_NODE
    else:
        new_value_type = TYPE_LEAF
    res = {
        'path': path,
        'key': key,
        'old_value': old_value,
        'old_value_type': old_value_type,
        'new_value': new_value,
        'new_value_type': new_value_type,
        'status': status
    }
    return res


def compare_data(old_data, new_data, path):  # noqa: C901
    """
    Функция получает на вход два словаря с наборами параметров
    и путь к этим параметрам. Сверяет каждый параметр в этих словарях.
    Результат выводится в виде списка данных о статусах каждого параметра.
    ADDED - параметр добавлен в новый файл
    REMOVED - параметр удален из нового файла
    EQUAL - значения параметров одинаковые в обоих файлах
    NODE - параметр является вложенной структурой
    UPDATED - значение параметра изменено
    PASS - сравнение не выполнялось
    """
    sorted_keys = sorted(old_data.keys() | new_data.keys())
    diff = []
    for key in sorted_keys:
        if key not in old_data:
            status = ADDED
            old_value = None
            new_value = new_data[key]
        elif key not in new_data:
            status = REMOVED
            old_value = old_data[key]
            new_value = None
        elif isinstance(old_data[key], dict) and isinstance(
                new_data[key], dict):
            status = NODE
            new_value = new_data[key]
            old_value = old_data[key]
        elif old_data[key] == new_data[key]:
            status = EQUAL
            new_value = new_data[key]
            old_value = old_data[key]
        elif old_data[key] != new_data[key]:
            status = UPDATED
            new_value = new_data[key]
            old_value = old_data[key]
        else:
            assert True, 'Что-то пошло не по плану :('
        rec = get_compare_status(path, key, old_value, new_value, status)
        diff.append(rec)
        if status == NODE:
            new_path = path + [key]
            diff.extend(compare_data(old_value, new_value, new_path))
    return diff
