import os
import json

from models.game_state import GameState

class JSONStorage:
    def __init__(self, path):
        self.path = path

    def exists(self):
        return os.path.isfile(self.path)

    def read(self):
        if self.exists() is False:
            raise FileNotFoundError()

        with open(self.path, "r") as f:
            json_data = json.load(f)
            return json_data

    def write_data(self, data):
        json_data = data
        with open(self.path, "w") as f:
            json.dump(json_data, f)

def new_storage(file_path, init_data):
    storage = JSONStorage(file_path)

    storage_exists = storage.exists()
    if storage_exists is False:
        init_data = dict()
        init_data["players"] = []
        init_data["state"] = GameState.Pending.value
        print(init_data)
        storage.write_data(init_data)

    return storage
