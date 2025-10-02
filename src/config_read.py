'''Reads the configuration from a YAML file and returns it as a dictionary.'''

import os
from typing import Any, Dict, Tuple
import yaml  # pylint: disable=import-error


def read_config() -> Tuple[Dict[Any, Any], bool]:
    '''
    Reads the configuration from a YAML file and returns it as a dictionary.
    '''
    try:
        with open('config/config.yaml', 'r', encoding='utf-8') as file:
            raw_config = file.read()
            # Replace environment variable placeholders with actual values
            expanded = os.path.expandvars(raw_config)
            loaded_yaml = yaml.safe_load(expanded)
            print(loaded_yaml)
    except FileNotFoundError:
        print("Configuration file not found.")
        return {}, False

    return loaded_yaml, True
