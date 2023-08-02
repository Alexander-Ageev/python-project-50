import json
import yaml
from gendiff.tools.read_data import JSON, YAML


DATA_TYPE = {
    JSON: json.loads,
    YAML: yaml.safe_load,
}


def parse_data(data, data_type='json'):
    """Парсинг полученных JSON и YAML данных"""
    parser = DATA_TYPE.get(data_type, None)
    return parser(data)
