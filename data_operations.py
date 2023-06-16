import json
from bookmark_collection import BookmarkCollection 


def restore_data():
    with open("/home/bani/code/python/EnderPearl/data.json", "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}


def save_data(bks: BookmarkCollection):
    with open("/home/bani/code/python/EnderPearl/data.json", "w") as f:
        json.dump(bks.get_dict(), f)
