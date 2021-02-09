import room_assignment
import teacher_assignment
import window_classification
import genetic_algorithm
from room import Room
from teacher import Teacher
from simple_group import SimpleGroup
import exporter

time_windows = genetic_algorithm.time_windows


def generateTimetable(timetable_datas, rooms, teachers, simple_groups):
    for room in range(len(rooms)):
        rooms[room] = Room(rooms[room]['name'], rooms[room]['capacity'], rooms[room]['subjects'])
    for teacher in range(len(teachers)):
        teachers[teacher] = Teacher(teachers[teacher]['name'], teachers[teacher]['subjects'],
                                    teachers[teacher]['balance'], teachers[teacher]['extremisms'],
                                    teachers[teacher]['begin_time'], teachers[teacher]['end_time'])
    for group in range(len(simple_groups)):
        simple_groups[group] = SimpleGroup(simple_groups[group]['name'], simple_groups[group]['grade'],
                                           simple_groups[group]['subjects'], simple_groups[group]['headcount'])

    groups = room_assignment.main(simple_groups, rooms)
    if timetable_datas['add_manually'] is False:
        groups = teacher_assignment.main(groups, teachers)
    periods = window_classification.main(groups, teachers)
    periods = genetic_algorithm.main(teachers, periods)

    group_timetables = []
    for group in range(len(simple_groups)):
        timetable = {'name': simple_groups[group].name, 'days': [], 'periods': [],
                     'subjects': [], 'rooms': [], 'teachers': []}
        for period in range(len(periods)):
            for assignment in range(len(periods[period])):
                if periods[period]['assignments'][assignment].name == simple_groups[group].name:
                    timetable['days'].append(periods[period]['day'])
                    timetable['periods'].append(periods[period]['period'])
                    timetable['subjects'].append(periods[period]['assignments'][assignment].subject)
                    timetable['rooms'].append(periods[period]['assignments'][assignment].room)
                    timetable['teachers'].append(periods[period]['assignments'][assignment].teacher)
        group_timetables.append(timetable)

    teacher_timetables = []
    for teacher in range(len(teachers)):
        timetable = {'name': teachers[teacher].name, 'days': [], 'periods': [],
                     'subjects': [], 'rooms': [], 'groups': []}
        for period in range(len(periods)):
            for assignment in range(len(periods[period])):
                if periods[period]['assignments'][assignment].teacher == teachers[teacher].name:
                    timetable['days'].append(periods[period]['day'])
                    timetable['periods'].append(periods[period]['period'])
                    timetable['subjects'].append(periods[period]['assignments'][assignment].subject)
                    timetable['rooms'].append(periods[period]['assignments'][assignment].room)
                    timetable['groups'].append(periods[period]['assignments'][assignment].name)
        teacher_timetables.append(timetable)

    room_timetables = []
    for room in range(len(rooms)):
        timetable = {'name': rooms[room].name, 'days': [], 'periods': [],
                     'subjects': [], 'teachers': [], 'groups': []}
        for period in range(len(periods)):
            for assignment in range(len(periods[period])):
                if periods[period]['assignments'][assignment].room == rooms[room].name:
                    timetable['days'].append(periods[period]['day'])
                    timetable['periods'].append(periods[period]['period'])
                    timetable['subjects'].append(periods[period]['assignments'][assignment].subject)
                    timetable['teachers'].append(periods[period]['assignments'][assignment].teacher)
                    timetable['groups'].append(periods[period]['assignments'][assignment].name)
        room_timetables.append(timetable)

    for timetable in range(len(group_timetables)):
        sortGroupTimetable(group_timetables[timetable])
    for timetable in range(len(teacher_timetables)):
        sortTeacherTimetable(teacher_timetables[timetable])
    for timetable in range(len(room_timetables)):
        sortRoomTimetable(room_timetables[timetable])

    exporter.exportTimetables(group_timetables, teacher_timetables, room_timetables)


def sortGroupTimetable(timetable):
    counter = 0
    for day in time_windows.keys():
        for period in range(len(time_windows['day'])):
            for assignment in range(len(timetable['periods'])):
                if timetable['periods'][assignment] == time_windows['day'][period] and\
                   timetable['days'][assignment] == day:
                    tmp = {'day': timetable['days'][counter], 'period': timetable['periods'][counter],
                           'subject': timetable['subjects'][counter], 'room': timetable['rooms'][counter],
                           'teacher': timetable['teachers'][counter]}
                    timetable['days'][counter] = timetable['days'][assignment]
                    timetable['periods'][counter] = timetable['periods'][assignment]
                    timetable['subjects'][counter] = timetable['subjects'][assignment]
                    timetable['rooms'][counter] = timetable['rooms'][assignment]
                    timetable['teachers'][counter] = timetable['teachers'][assignment]
                    timetable['days'][assignment] = tmp['day']
                    timetable['periods'][assignment] = tmp['period']
                    timetable['subjects'][assignment] = tmp['subject']
                    timetable['rooms'][assignment] = tmp['room']
                    timetable['teachers'][assignment] = tmp['teacher']
                    counter += 1


def sortTeacherTimetable(timetable):
    counter = 0
    for day in time_windows.keys():
        for period in range(len(time_windows['day'])):
            for assignment in range(len(timetable['periods'])):
                if timetable['periods'][assignment] == time_windows['day'][period] and\
                   timetable['days'][assignment] == day:
                    tmp = {'day': timetable['days'][counter], 'period': timetable['periods'][counter],
                           'subject': timetable['subjects'][counter], 'room': timetable['rooms'][counter],
                           'group': timetable['groups'][counter]}
                    timetable['days'][counter] = timetable['days'][assignment]
                    timetable['periods'][counter] = timetable['periods'][assignment]
                    timetable['subjects'][counter] = timetable['subjects'][assignment]
                    timetable['rooms'][counter] = timetable['rooms'][assignment]
                    timetable['groups'][counter] = timetable['groups'][assignment]
                    timetable['days'][assignment] = tmp['day']
                    timetable['periods'][assignment] = tmp['period']
                    timetable['subjects'][assignment] = tmp['subject']
                    timetable['rooms'][assignment] = tmp['room']
                    timetable['groups'][assignment] = tmp['group']
                    counter += 1


def sortRoomTimetable(timetable):
    counter = 0
    for day in time_windows.keys():
        for period in range(len(time_windows['day'])):
            for assignment in range(len(timetable['periods'])):
                if timetable['periods'][assignment] == time_windows['day'][period] and \
                        timetable['days'][assignment] == day:
                    tmp = {'day': timetable['days'][counter], 'period': timetable['periods'][counter],
                           'subject': timetable['subjects'][counter], 'group': timetable['groups'][counter],
                           'teacher': timetable['teachers'][counter]}
                    timetable['days'][counter] = timetable['days'][assignment]
                    timetable['periods'][counter] = timetable['periods'][assignment]
                    timetable['subjects'][counter] = timetable['subjects'][assignment]
                    timetable['groups'][counter] = timetable['groups'][assignment]
                    timetable['teachers'][counter] = timetable['teachers'][assignment]
                    timetable['days'][assignment] = tmp['day']
                    timetable['periods'][assignment] = tmp['period']
                    timetable['subjects'][assignment] = tmp['subject']
                    timetable['groups'][assignment] = tmp['group']
                    timetable['teachers'][assignment] = tmp['teacher']
                    counter += 1
