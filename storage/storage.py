from storage.json_storage import JSONStorage


class Storage:
    def __init__(self, storage: JSONStorage):
        self.storage = storage