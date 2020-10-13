import csv
from klass import Class
from room import Room
from teacher import Teacher


def load_classes(csv_path):
    classes = []
    with open(csv_path) as csv_classes:
        reader = csv.reader(csv_classes, delimiter=';')
        for row in reader:
            row[1] = int(row[1])
            row[4] = int(row[4])
            row[5] = int(row[5])
            classes.append(row)
    for i in range(len(classes)):
        classes[i] = Class(classes[i][0], classes[i][1], classes[i][2], classes[i][3], classes[i][4], classes[i][5], i)
    return classes


def load_rooms(csv_path):
    rooms = []
    with open(csv_path) as csv_rooms:
        reader = csv.reader(csv_rooms, delimiter=';')
        for row in reader:
            row[1] = int(row[1])
            rooms.append(row)
    for i in range(len(rooms)):
        rooms[i] = Room(rooms[i][0], rooms[i][1])
    return rooms


def load_teachers(csv_path):
    teachers = []
    with open(csv_path) as csv_teachers:
        reader = csv.reader(csv_teachers, delimiter=';')
        for row in reader:
            teachers.append(row)
    for i in range(len(teachers)):
        teachers[i] = Teacher(teachers[i][0], teachers[i][1], teachers[i][2])
    return teachers
