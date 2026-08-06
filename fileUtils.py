import json


def openFile(name, mode="r", encodeValue="utf-8", dump=""):
    with open(name, mode, encoding=encodeValue) as f:
        if mode == "r":
            file = json.load(f)
        elif mode == "w":
            file = json.dump(dump, f, indent=4)
        return file
