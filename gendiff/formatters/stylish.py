from gendiff.tools import (
    ADDED, EQUAL, PASS, REMOVED,
    UPDATED, NODE, TYPE_NODE,
)
from gendiff.tools.get_difference import get_children

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


def stylish(data, style=DEFAULT_STYLE):
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
        for i in range(ex_level - level):
            stilysh_data.append(indent * (ex_level - i) + style['block close'])
        if value_type == TYPE_NODE:
            value = style['block open']
        stilysh_data.append(f'{indent*level}{status_symbol}{key}: {value}')
        ex_level = level
    for i in range(level + 1):
        stilysh_data.append(indent * (level - i) + style['block close'])
    return '\n'.join(stilysh_data)
