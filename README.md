# Gendiff

### Hexlet tests and linter status:

[![Actions Status](https://github.com/Alexander-Ageev/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/Alexander-Ageev/python-project-50/actions)
[![Maintainablity](https://api.codeclimate.com/v1/badges/b32e97d7362b0b34962f/maintainability)](https://codeclimate.com/github/Alexander-Ageev/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/b32e97d7362b0b34962f/test_coverage)](https://codeclimate.com/github/Alexander-Ageev/python-project-50/test_coverage)
[![my-CI](https://github.com/Alexander-Ageev/python-project-50/actions/workflows/my-CI.yml/badge.svg?branch=main&event=status)](https://github.com/Alexander-Ageev/python-project-50/actions/workflows/my-CI.yml)
## Description

Searches for the difference in the parameters of two configuration files. Accepts input files in json or yaml formats. Returns the result in styilish, plain or json formats.

## Comand

> gendiff [--format] old_file new_file


## Format examples

---
### Stylish
---
```
{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}
```
where:

`'-'` The parameter is removed from new file.  
`'+'` The parameter is added to a new file.  
`' '` The parameters are equal in both files.  

---
### Plain
---
```
Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]
```
---
### JSON
---
```
{'common': {'setting3': None, 'setting6': {'doge': {'wow': 'so much'}, 'ops': 'vops'}, 'follow': False, 'setting4': 'blah blah', 'setting5': {'key5': 'value5'}, delete: ['setting2']}, 'group1': {'baz': 'bars', 'nest': 'str'}, 'group3': {'deep': {'id': {'number': 45}}, 'fee': 100500}, delete: ['group2']}
```





## Links

This project was built using these tools:

| Tool                                                                        | Description                                             |
|-----------------------------------------------------------------------------|---------------------------------------------------------|
| [poetry](https://poetry.eustace.io/)                                        | "Python dependency management and packaging made easy"  |
| [Py.Test](https://pytest.org)                                               | "A mature full-featured Python testing tool"            |
| [Pytest-cov](https://pypi.org/project/pytest-cov/)                          | "This plugin produces coverage reports"                 |
| [Flake8](https://flake8.pycqa.org/en/latest/index.html)                     | "Linter"                                                |
| [pyyaml](https://pypi.org/project/PyYAML/)                                  | "Library for read YAML files"                           |
| [jsondiff](https://pypi.org/project/jsondiff/)                              | "Return difference between two data in json format"     |

### Example:

<a href="https://asciinema.org/a/noqwMh5V4EiMlpyCuX5uH2nmM" target="_blank"><img src="https://asciinema.org/a/noqwMh5V4EiMlpyCuX5uH2nmM.svg" /></a>