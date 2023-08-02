from gendiff.tools.generator import generate_diff
import pytest


SIMPLE = 'tests/fixtures/simple_file'
SIMPLE_RESULT_ST = 'tests/fixtures/simple_result(stylish).txt'
DEEP = 'tests/fixtures/deep_file'
DEEP_RESULT_ST = 'tests/fixtures/deep_result(stylish).txt'
DEEP_RESULT_PL = 'tests/fixtures/deep_result(plain).txt'
DEEP_RESULT_JSON = 'tests/fixtures/deep_result(json).txt'


@pytest.mark.parametrize(
    "old_file, new_file, formatter, expected", [
        (SIMPLE + '1.json', SIMPLE + '2.json', 'stylish', SIMPLE_RESULT_ST),
        (SIMPLE + '1.yaml', SIMPLE + '2.yml', 'stylish', SIMPLE_RESULT_ST),
        (DEEP + '1.json', DEEP + '2.json', 'stylish', DEEP_RESULT_ST),
        (DEEP + '1.yaml', DEEP + '2.yml', 'stylish', DEEP_RESULT_ST),
        (DEEP + '1.yaml', DEEP + '2.yml', 'plain', DEEP_RESULT_PL),
        (DEEP + '1.yaml', DEEP + '2.yml', 'json', DEEP_RESULT_JSON),
    ]
)
def test_gendiff(old_file, new_file, formatter, expected):
    with open(expected) as file:
        res = file.read()
    assert generate_diff(old_file, new_file, formatter) == res
