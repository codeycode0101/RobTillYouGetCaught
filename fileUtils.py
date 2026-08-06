import json


def openFile(name, mode="r", encodeValue="utf-8", dump=""):
    with open(name, mode, encoding=encodeValue) as f:
        file = None
        if mode == "r":
            file = json.load(f)
        elif mode == "w":
            json.dump(dump, f, indent=4)
        return file
