import data_loader
import math

classes = data_loader.load_classes(r'C:\Users\Brendi\Documents\Szakdoga\osztalyok.csv')
rooms = data_loader.load_rooms(r'C:\Users\Brendi\Documents\Szakdoga\tantermek.csv')
NUM_CLASSES = len(classes)
NUM_ROOMS = len(rooms)

simple_classes = []
for i in range(NUM_CLASSES):
    boole = False
    for k in range(len(simple_classes)):
        if classes[i].name == simple_classes[k].name:
            boole = True
            break
    if not boole:
        simple_classes.append(classes[i])

pairings = [[] for _ in range(len(simple_classes))]
idles = [[] for _ in range(len(simple_classes))]
for i in range(len(simple_classes)):
    for j in range(NUM_ROOMS):
        if simple_classes[i].headcount <= rooms[j].capacity:
            pairings[i].append(1)
            idles[i].append(rooms[j].capacity - simple_classes[i].headcount)
        else:
            pairings[i].append(0)
            idles[i].append(math.nan)

seated_rooms = []
seated_types = []
for i in range(len(simple_classes)):
    min = math.inf
    minindex = math.nan
    type = ""
    for j in range(NUM_ROOMS):
        boole = False
        if (pairings[i][j] == 1) & (idles[i][j] < min):
            for k in range(len(seated_rooms)):
                if (rooms[j] == seated_rooms[k]) and (simple_classes[i].type == seated_types[k]):
                    boole = True
                    break
            if not boole:
                min = idles[i][j]
                minindex = j
                type = simple_classes[i].type
                simple_classes[i].room = rooms[j].name
        if j == NUM_ROOMS - 1:
            seated_rooms.append(rooms[minindex])
            seated_types.append(type)

for i in range(len(simple_classes)):
    for j in range(NUM_CLASSES):
        if classes[j].name == simple_classes[i].name:
            classes[j].room = simple_classes[i].room
            print(classes[j].name, classes[j].room)

