from gendiff.scripts.gendiff import generate_diff


def test_simple_json():
    data1 = 'gendiff/tests/fixtures/simple_file1.json'
    data2 = 'gendiff/tests/fixtures/simple_file2.json'
    with open('gendiff/tests/fixtures/simple_result(stylish).txt') as file:
        res = file.read()
    assert generate_diff(data1, data2) == res


def test_simple_yaml():
    data1 = 'gendiff/tests/fixtures/simple_file1.yaml'
    data2 = 'gendiff/tests/fixtures/simple_file2.yml'
    with open('gendiff/tests/fixtures/simple_result(stylish).txt') as file:
        res = file.read()
    assert generate_diff(data1, data2) == res


def test_deep_json():
    data1 = 'gendiff/tests/fixtures/deep_file1.json'
    data2 = 'gendiff/tests/fixtures/deep_file2.json'
    with open('gendiff/tests/fixtures/deep_result(stylish).txt') as file:
        res = file.read()
    assert generate_diff(data1, data2) == res


def test_deep_yaml():
    data1 = 'gendiff/tests/fixtures/deep_file1.yaml'
    data2 = 'gendiff/tests/fixtures/deep_file2.yml'
    with open('gendiff/tests/fixtures/deep_result(stylish).txt') as file:
        res = file.read()
    assert generate_diff(data1, data2) == res


def test_deep_plain():
    data1 = 'gendiff/tests/fixtures/deep_file1.yaml'
    data2 = 'gendiff/tests/fixtures/deep_file2.yml'
    with open('gendiff/tests/fixtures/deep_result(plain).txt') as file:
        res = file.read()
    assert generate_diff(data1, data2, 'plain') == res
