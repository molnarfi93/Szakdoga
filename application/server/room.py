import json


class Room:
    def __init__(self, name, capacity, subjects):
        self.name = name
        self.capacity = capacity
        self.subjects = subjects


def load_rooms(json_path):
    rooms = []
    with open(json_path) as json_file:
        rooms_data = json.load(json_file)['rooms']
    for name, datas in rooms_data.items():
        room = Room(name, **datas)
        rooms.append(room)
    return rooms
