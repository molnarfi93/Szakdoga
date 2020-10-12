import csv

from timetable.teachers import Teacher


def load_teachers(csv_path):
    """
    Load teacher data from a CSV file.
    :param csv_path: path of the CSV file
    :return: list of teachers
    """
    teachers = []
    with open(csv_path) as csv_teachers:
        reader = csv.reader(csv_teachers, delimiter=';')
        for row in reader:
            name, subject_1, subject_2 = row
            teacher = Teacher(name, [subject_1, subject_2])
            teachers.append(teacher)
    return teachers



