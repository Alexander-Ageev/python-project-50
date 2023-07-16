from gendiff.tools.get_difference import get_difference
from gendiff.tools import (
    ADDED, EQUAL, PASS, REMOVED,
    UPDATED, NODE,
)


def get_correct_value(value):
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


def make_plain(old_data, new_data):  # noqa: C901
    data = get_difference(old_data, new_data, [])
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
