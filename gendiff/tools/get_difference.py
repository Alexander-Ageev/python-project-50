from gendiff.tools import (
    ADDED, EQUAL, PASS, REMOVED,
    UPDATED, NODE, TYPE_NODE, TYPE_LEAF
)


def get_diff_rec(path, key, old_value, new_value=None, status=PASS):
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


def get_difference(old_data, new_data, path):  # noqa: C901
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
        rec = get_diff_rec(path, key, old_value, new_value, status)
        diff.append(rec)
        if status == NODE:
            new_path = path + [key]
            diff.extend(get_difference(old_value, new_value, new_path))
    return diff
