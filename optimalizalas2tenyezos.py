import data_loader
import math

groups = data_loader.load_groups(r'C:\Users\Brendi\Documents\Szakdoga\osztalyok.json')
rooms = data_loader.load_rooms(r'C:\Users\Brendi\Documents\Szakdoga\tantermek.json')
NUM_GROUPS = len(groups)
NUM_ROOMS = len(rooms)

simple_groups = []
for group in range(NUM_GROUPS):
    boole = False
    for simple_group in range(len(simple_groups)):
        if groups[group].name == simple_groups[simple_group].name:
            boole = True
            break
    if not boole:
        simple_groups.append(groups[group])

pairings = [[] for _ in range(len(simple_groups))]
idles = [[] for _ in range(len(simple_groups))]
for simple_group in range(len(simple_groups)):
    for room in range(NUM_ROOMS):
        if simple_groups[simple_group].headcount <= rooms[room].capacity:
            pairings[simple_group].append(1)
            idles[simple_group].append(rooms[room].capacity - simple_groups[simple_group].headcount)
        else:
            pairings[simple_group].append(0)
            idles[simple_group].append(math.nan)

seated_rooms = []
seated_types = []
for simple_group in range(len(simple_groups)):
    min = math.inf
    minindex = math.nan
    type = ""
    for room in range(NUM_ROOMS):
        boole = False
        if (pairings[simple_group][room] == 1) & (idles[simple_group][room] < min):
            for seated_room in range(len(seated_rooms)):
                if (rooms[room] == seated_rooms[seated_room]) and (simple_groups[simple_group].type == seated_types[seated_room]):
                    boole = True
                    break
            if not boole:
                min = idles[simple_group][room]
                minindex = room
                type = simple_groups[simple_group].type
                simple_groups[simple_group].room = rooms[room].name
        if room == NUM_ROOMS - 1:
            seated_rooms.append(rooms[minindex])
            seated_types.append(type)

for simple_group in range(len(simple_groups)):
    for group in range(NUM_GROUPS):
        if groups[group].name == simple_groups[simple_group].name:
            groups[group].room = simple_groups[simple_group].room
            print(groups[group].name, groups[group].room)
