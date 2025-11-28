from configparser import ConfigParser
 
def load_config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename, encoding='utf-8')
 
    config = {}
    if parser.has_section(section):
        for key, value in parser.items(section):
            config[key] = value
        return config
    else:
        raise Exception(f"Section {section} not found")
 
if __name__ == '__main__':
    print(load_config())


from configparser import ConfigParser
from pathlib import Path
 
BASE_DIR = Path(__file__).resolve().parent
 
 
def load_config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
 
    filepath = BASE_DIR / filename
 
    if not filepath.exists():
        raise FileNotFoundError(f"Config file not found: {filepath}")
 
    parser.read(filepath, encoding='utf-8')
 
    if not parser.has_section(section):
        raise Exception(f"Section {section} not found in {filepath}")
 
    return {k: v for k, v in parser.items(section)}
 
 