from gendiff.scripts.gendiff import generate_diff, get_data


def test_json():
    data1 = get_data('gendiff/tests/fixtures/file1.json')
    data2 = get_data('gendiff/tests/fixtures/file2.json')
    with open('gendiff/tests/fixtures/result.txt') as file:
        res = file.read()
    assert generate_diff(data1, data2) == res


def test_yaml():
    data1 = get_data('gendiff/tests/fixtures/file1.yaml')
    data2 = get_data('gendiff/tests/fixtures/file2.yml')
    with open('gendiff/tests/fixtures/result.txt') as file:
        res = file.read()
    assert generate_diff(data1, data2) == res
