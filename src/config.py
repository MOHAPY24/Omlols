import json

def get_config():
    with open("config/config.json", 'r') as f:
        return json.loads(f.read())