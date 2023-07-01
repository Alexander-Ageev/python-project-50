from gendiff.tools import (
    ADDED, EQUAL, PASS, REMOVED,
    UPDATED, NODE,
)


def get_correct_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    elif isinstance(value, str):
        return f'\'{value}\''
    else:
        return value


def plain(data):
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
