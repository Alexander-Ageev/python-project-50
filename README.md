# Gendiff

Searches for the difference in the parameters of two configuration files. Returns the result as a string of 
the form:

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
"-" indicates the presence or difference of a parameter in file1.
"+" indicates the presence or difference of a parameter in file2.
" " means that there is no difference in the parameters.

### Hexlet tests and linter status:
[![Actions Status](https://github.com/Alexander-Ageev/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/Alexander-Ageev/python-project-50/actions)
[![Maintainablity](https://api.codeclimate.com/v1/badges/b32e97d7362b0b34962f/maintainability)](https://codeclimate.com/github/Alexander-Ageev/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/b32e97d7362b0b34962f/test_coverage)](https://codeclimate.com/github/Alexander-Ageev/python-project-50/test_coverage)

### Links

This project was built using these tools:

| Tool                                                                        | Description                                             |
|-----------------------------------------------------------------------------|---------------------------------------------------------|
| [poetry](https://poetry.eustace.io/)                                        | "Python dependency management and packaging made easy"  |
| [Py.Test](https://pytest.org)                                               | "A mature full-featured Python testing tool"            |


### Example:

<a href="https://asciinema.org/a/noqwMh5V4EiMlpyCuX5uH2nmM" target="_blank"><img src="https://asciinema.org/a/noqwMh5V4EiMlpyCuX5uH2nmM.svg" /></a>