from gendiff.tools import (
    ADDED, EQUAL, PASS, REMOVED,
    UPDATED, NODE, TYPE_NODE, TYPE_LEAF
)


def get_diff_rec(
        path, key, old_value=None, new_value=None,
        status=PASS):
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


def get_children(data, path):
    childrens = []
    if not isinstance(data, dict):
        return childrens
    keys = sorted(data.items(), reverse=True)
    for key, value in keys:
        childrens.append(get_diff_rec(path, key, value))
    return childrens


def get_difference(old_data, new_data, path):
    sorted_keys = sorted(old_data.keys() | new_data.keys())
    diff = []
    for key in sorted_keys:
        if key not in old_data:
            rec = get_diff_rec(path, key, None, new_data[key], ADDED)
            diff.append(rec)
        elif key not in new_data:
            rec = get_diff_rec(path, key, old_data[key], status=REMOVED)
            diff.append(rec)
        elif isinstance(old_data[key], dict) and isinstance(new_data[key], dict):
            rec = get_diff_rec(path, key, old_data[key], new_data[key], NODE)
            diff.append(rec)
            new_path = path + [key]
            diff.extend(get_difference(old_data[key], new_data[key], new_path))
        elif old_data[key] == new_data[key]:
            rec = get_diff_rec(path, key, old_data[key], new_data[key], EQUAL)
            diff.append(rec)
        elif old_data[key] != new_data[key]:
            rec = get_diff_rec(path, key, old_data[key], new_data[key], UPDATED)
            diff.append(rec)
        else:
            assert True, 'Что-то пошло не по плану :('
    return diff
