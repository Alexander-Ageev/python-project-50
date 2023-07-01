from gendiff.scripts.gendiff import generate_diff
from gendiff.tools.get_data import get_data


def test_simple_json():
    data1 = get_data('gendiff/tests/fixtures/simple_file1.json')
    data2 = get_data('gendiff/tests/fixtures/simple_file2.json')
    with open('gendiff/tests/fixtures/simple_result(stylish).txt') as file:
        res = file.read()
    assert generate_diff(data1, data2) == res


def test_simple_yaml():
    data1 = get_data('gendiff/tests/fixtures/simple_file1.yaml')
    data2 = get_data('gendiff/tests/fixtures/simple_file2.yml')
    with open('gendiff/tests/fixtures/simple_result(stylish).txt') as file:
        res = file.read()
    assert generate_diff(data1, data2) == res


def test_deep_json():
    data1 = get_data('gendiff/tests/fixtures/deep_file1.json')
    data2 = get_data('gendiff/tests/fixtures/deep_file2.json')
    with open('gendiff/tests/fixtures/deep_result(stylish).txt') as file:
        res = file.read()
    assert generate_diff(data1, data2) == res


def test_deep_yaml():
    data1 = get_data('gendiff/tests/fixtures/deep_file1.yaml')
    data2 = get_data('gendiff/tests/fixtures/deep_file2.yml')
    with open('gendiff/tests/fixtures/deep_result(stylish).txt') as file:
        res = file.read()
    assert generate_diff(data1, data2) == res


def test_deep_plain():
    data1 = get_data('gendiff/tests/fixtures/deep_file1.yaml')
    data2 = get_data('gendiff/tests/fixtures/deep_file2.yml')
    with open('gendiff/tests/fixtures/deep_result(plain).txt') as file:
        res = file.read()
    assert generate_diff(data1, data2, 'plain') == res
