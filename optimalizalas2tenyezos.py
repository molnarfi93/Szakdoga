from osztalyok import Room, Class
import csv
import math
global NUM_ROOMS
NUM_ROOMS = 30
global NUM_CLASSES
NUM_CLASSES = 220
global rooms
rooms = []
global classes
classes = []
simple_classes = []
with open(r'C:\Users\Brendi\Documents\Szakdoga\tantermek.csv')as csv_rooms:
    reader = csv.reader(csv_rooms, delimiter=';')
    for row in reader:
        row[1] = int(row[1])
        rooms.append(row)
with open(r'C:\Users\Brendi\Documents\Szakdoga\osztalyok.csv') as csv_classes:
    reader = csv.reader(csv_classes, delimiter=';')
    for row in reader:
        row[1] = int(row[1])
        row[4] = int(row[4])
        row[5] = int(row[5])
        classes.append(row)
for i in range (NUM_ROOMS):
    rooms[i] = Room(rooms[i][0], rooms[i][1])
for i in range (NUM_CLASSES):
    classes[i] = Class(classes[i][0], classes[i][1], classes[i][2], classes[i][3], classes[i][4], classes[i][5], i)
for i in range (NUM_CLASSES):
    boole = False
    for k in range (len(simple_classes)):
        if classes[i].name == simple_classes[k].name:
            boole = True
            break
    if not boole:
        simple_classes.append(classes[i])
pairings = [[] for _ in range (len(simple_classes))]
idles = [[] for _ in range (len(simple_classes))]
for i in range (len(simple_classes)):
    for j in range (NUM_ROOMS):
        if simple_classes[i].headcount <= rooms[j].capacity:
            pairings[i].append(1)
            idles[i].append(rooms[j].capacity - simple_classes[i].headcount)
        else:
            pairings[i].append(0)
            idles[i].append(math.nan)
seated_rooms = []
seated_types = []
for i in range (len(simple_classes)):
    min = 1000
    minindex = math.nan
    type = ""
    for j in range (NUM_ROOMS):
        boole = False
        if (pairings[i][j] == 1) & (idles[i][j] < min):
            for k in range (len(seated_rooms)):
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
for i in range (len(simple_classes)):
    for j in range (NUM_CLASSES):
        if classes[j].name == simple_classes[i].name:
            classes[j].room = simple_classes[i].room
            print(classes[j].name, classes[j].room)

