import simplegroup
from group import Group
import room
import math
import random

simple_groups = simplegroup.load_groups(r'C:\Users\Brendi\Documents\Szakdoga\osztalyok.json')
rooms = room.load_rooms(r'C:\Users\Brendi\Documents\Szakdoga\tantermek.json')


def createTable(groups):
    rows = []
    for group in groups:
        for subject in group.subjects:
            row = Group(group.name, group.grade, subject.name, subject.type, subject.weekly_periods, group.headcount)
            rows.append(row)
    return rows


groups = createTable(simple_groups)
pairings = [[] for _ in range(len(simple_groups))]
idles = [[] for _ in range(len(simple_groups))]
for simple_group in range(len(simple_groups)):
    for room in range(len(rooms)):
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
    for room in range(len(rooms)):
        ok = False
        if (pairings[simple_group][room] == 1) and (idles[simple_group][room] < min):
            for seated_room in range(len(seated_rooms)):
                if (rooms[room] == seated_rooms[seated_room]) and (simple_groups[simple_group].subjects[0].type == seated_types[seated_room]):
                    ok = True
                    break
            if not ok:
                min = idles[simple_group][room]
                minindex = room
                type = simple_groups[simple_group].subjects[0].type
                simple_groups[simple_group].room = rooms[room]
        if room == len(rooms) - 1:
            seated_rooms.append(rooms[minindex])
            seated_types.append(type)

for simple_group in range(len(simple_groups)):
    for group in range(len(groups)):
        if groups[group].name == simple_groups[simple_group].name:
            ok = False
            for subject in range (len(simple_groups[simple_group].room.subjects)):
                if groups[group].subject == simple_groups[simple_group].room.subjects[subject]:
                    ok = True
                    break
            if not ok:
                ok = True
                for room in range(len(rooms)):
                    for subject in range(len(rooms[room].subjects)):
                        if groups[group].subject == rooms[room].subjects[subject]:
                            ok = False
                            break
            counter = 0
            if not ok:
                paired = False
                while not paired and counter != 10000:
                    counter += 1
                    rand_room = rooms[random.randint(0, len(rooms) - 1)]
                    for subject in range(len(rand_room.subjects)):
                        if (groups[group].subject == rand_room.subjects[subject]) and (groups[group].headcount <= rand_room.capacity):
                            groups[group].room = rand_room.name
                            paired = True
                            break
            if ok or counter == 10000:
                groups[group].room = simple_groups[simple_group].room.name
            print(groups[group].name, groups[group].subject, groups[group].room)



