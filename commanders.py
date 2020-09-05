# commanders.py
import json
import random


def build_commander_list():
    wd = os.path.dirname(__file__)
    file_name = "cdmers.json"
    file_path = os.path.join(wd, file_name)
    with open(file_path, "r") as read_file:
        return json.load(read_file)


def choose_commander(commander_list):
    return random.choice(commander_list)
