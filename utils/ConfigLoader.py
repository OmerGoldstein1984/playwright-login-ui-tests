import json

class ConfigLoader:
    def __init__(self, dev):
        self.config_file_path = f"config/{dev}.json"

    def load_config(self):
        with open(self.config_file_path) as f:
            return json.load(f)

    def get_property(self, key):
        return self.load_config()[key]