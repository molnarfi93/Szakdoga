from klass import Class
from room import Room
from teacher import Teacher
import json


@staticmethod
def load_classes(json_path):
    classes = []
    with open(json_path) as json_file:
        classes_data = json.load(json_file)['classes']
    for no, datas in classes_data.items():
        klass = Class(no, datas['name'], datas['grade'], datas['subject'], datas['weekly_periods'], datas['headcount'])
        classes.append(klass)
    return classes


@staticmethod
def load_rooms(json_path):
    rooms = []
    with open(json_path) as json_file:
        classes_data = json.load(json_file)['rooms']
    for name, datas in classes_data.items():
        room = Room(name, datas['capacity'])
        rooms.append(room)
    return rooms


@staticmethod
def load_teachers(json_path):
    teachers = []
    with open(json_path) as json_file:
        classes_data = json.load(json_file)['teachers']
    for name in classes_data.items():
        teacher = Teacher(name)
        for subject_name in classes_data['subjects'].items():
            subject = subject_name
            teacher.subjects.append(subject)
        teachers.append(teacher)
    return teacher
