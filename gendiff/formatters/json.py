from jsondiff import diff


def make_json(old_data, new_data):
    return str(diff(old_data, new_data))
