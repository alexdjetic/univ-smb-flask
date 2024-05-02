import json


class DataParser:

    def __init__(self, file: str) -> None:
        self._file: str = file
        self._extraction_status: bool = False
        self._data: list = []
        self.extract()

    def __repr__(self) -> str:
        return f"file: {self._file}, extraction: {self._extraction_status}"

    def extract(self):
        try:
            with open("static/alias.json", "r") as f:
                self._data: list = json.load(f)

                if len(self._data) != 0:
                    self._extraction_status: bool = True
        except Exception as e:
            print(e)

    def extract_key(self, key: str) -> list | None:
        if self._data[0].get(key, None) is not None:
            return [self._data[i].get(key, None) for i in range(len(self._data))]
        else:
            return None