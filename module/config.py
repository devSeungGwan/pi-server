import json


class block_config:
    def __init__(self):
        self.json_src = "./config/config.json"
        self.config_data = {
            "capture_config": {
                "block_name": "F11S",
                "capture_root": "./capture",
                "width": 800,
                "height": 800,
            },
            "serial_config": {"serial_name": "/dev/ttyUSB0", "serial_port": 9600},
        }

    def get_data(self):
        with open(self.json_src, "r", encoding="utf-8") as json_file:
            json_data = json.load(json_file)
            self.config_data = json_data
            return json_data

    def set_data(self, key1, key2, value):
        with open(self.json_src, "r+") as json_file:
            json_data = json.load(json_file)
            json_data[key1][key2] = value
            json.dump(json_data, json_file, indent=4)