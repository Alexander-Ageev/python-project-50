from gendiff.tools.internal_representation import compare_data
from gendiff.tools.read_data import get_data
from gendiff.formatters.json import make_json
from gendiff.formatters.plain import make_plain
from gendiff.formatters.stylish import make_stylish
from gendiff.tools.parse_data import parse_data


DEFAULT_FORMATTER = 'stylish'
FORMATTERS = {
    'plain': make_plain,
    'json': make_json,
    'stylish': make_stylish
}


def generate_diff(old_file, new_file, format=DEFAULT_FORMATTER):
    old_data = parse_data(*get_data(old_file))
    new_data = parse_data(*get_data(new_file))
    data = compare_data(old_data, new_data, 0)
    for i in data:
        print(i)
    return FORMATTERS.get(format, DEFAULT_FORMATTER)(data)
