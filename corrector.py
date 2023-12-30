import logging

logging.basicConfig(level=logging.DEBUG)

def clean_key(key):
    """Remove special characters from the beginning of keys and values."""
    return key.lstrip("@#&")

def correct_yaml(yaml_data, level=0):
    """Recursively correct the YAML data."""
    logging.debug(f"Level {level}: Input data: {yaml_data}")

    if isinstance(yaml_data, dict):
        corrected_data = {
            clean_key(k): correct_yaml(v, level + 1)
            for k, v in yaml_data.items()
        }
    elif isinstance(yaml_data, list):
        corrected_data = [correct_yaml(item, level + 1) for item in yaml_data]
    else:
        corrected_data = yaml_data

    logging.debug(f"Level {level}: Corrected data: {corrected_data}")
    return corrected_data
