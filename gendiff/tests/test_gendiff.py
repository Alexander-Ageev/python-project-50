from gendiff.scripts.gendiff import generate_diff
import json
import pytest


def test_simple():
    with open('gendiff/tests/fixtures/file1.json') as file:
        data1 = json.load(file)
    with open('gendiff/tests/fixtures/file2.json') as file:
        data2 = json.load(file)
    with open('gendiff/tests/fixtures/result.txt') as file:
        res = file.read()
    assert generate_diff(data1, data2) == res
