"""
Модуль предназначен для чтения данных исходных файлов.
Функция работает только с файлами JSON и YAML.
"""


JSON = 'json'
YAML = 'yaml'


def get_data(file_path):
    # Чтение данных из файла
    ext = ''
    with open(file_path) as file:
        data = file.read()
    if file_path.lower().endswith('.json'):
        ext = JSON
    elif file_path.lower().endswith(('yml', 'yaml')):
        ext = YAML
    else:
        raise TypeError(
            'Gendiff используется только для работы с JSON и YAML файлами'
        )
    return data, ext
