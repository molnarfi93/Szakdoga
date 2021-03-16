from subject import Subject
import json


class SimpleGroup:
    def __init__(self, name, grade, subjects, headcount):
        self.name = name
        self.grade = grade
        self.subjects = []
        for subject_name, subject_data in subjects.items():
            subject = Subject(subject_name, **subject_data)
            self.subjects.append(subject)
        self.room = ""
        self.headcount = headcount


def load_groups(json_path):
    groups = []
    with open(json_path) as json_file:
        groups_data = json.load(json_file)['groups']
    for no, datas in groups_data.items():
        group = SimpleGroup(no, **datas)
        groups.append(group)
    return groups

