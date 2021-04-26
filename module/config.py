import json


class config:
    def __init__(self):
        self.json_src = "./config/config.json"
        self.config_data = {}

    def get_config(self):
        with open(self.json_src, "r", encoding="utf-8") as json_file:
            json_data = json.load(json_file)
            self.config_data = json_data
            return json_data

    def set_config(self, key, value):
        with open(self.json_src, "w") as json_file:        
            json_data = json.load(json_file)
            json_data[key] = value
            json.dump(json_data)