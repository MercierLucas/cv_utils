import json


def load_config(path):
    """Parse a json file and return dict"""
    with open(path, 'r') as f:
        return json.load(f)