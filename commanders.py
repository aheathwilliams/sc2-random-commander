# commanders.py
import json
import random


def build_commander_list():
    with open("cmders.json", "r") as read_file:
        return json.load(read_file)


def choose_commander(commander_list):
    return random.choice(commander_list)
