import base58
import hashlib
import json
import jsoncanon
import sys


def hash_file(name: str) -> str:
    with open(name) as opened:
        content = json.load(opened)
    assert isinstance(content, dict)
    if "@context" in content:
        del content["@context"]
    if "proof" in content:
        del content["proof"]
    canon = jsoncanon.canonicalize(content)
    return base58.b58encode(hashlib.sha256(canon).digest()).decode("ascii")


if __name__ == "__main__":
    paths = sys.argv[1:]
    for path in paths:
        print(f"{path}:", hash_file(path))
