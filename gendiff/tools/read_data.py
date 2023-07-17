"""
Модуль предназначен для чтения данных ииз разных форматов файлов.
Интерфейсом модуля является функция get_data, который объединяет в себе
разные функции чтения файлов.
"""
import json
import yaml


def get_data_from_json(file_path):
    #  Чтение данных из JSON файла
    with open(file_path) as file:
        data = json.load(file)
    return data


def get_data_from_yaml(file_path):
    # Чтение данных из YAML файла
    with open(file_path) as file:
        data = yaml.safe_load(file)
    return data


def get_data(file_path):
    # Чтение данных из соответствующего файла
    if file_path.lower().endswith('.json'):
        return get_data_from_json(file_path)
    elif file_path.lower().endswith(('yml', 'yaml')):
        return get_data_from_yaml(file_path)
    else:
        return None
