import room_assignment
import teacher_assignment
import window_classification
import genetic_algorithm
import exporter

time_windows = genetic_algorithm.time_windows


def generateTimetables(rooms, teachers, simple_groups):
    groups = room_assignment.main(simple_groups, rooms)
    groups = teacher_assignment.main(groups, teachers)
    periods = window_classification.main(groups, teachers)
    periods = genetic_algorithm.main(teachers, periods)

    group_timetables = []
    for group in range(len(simple_groups)):
        timetable = {'name': simple_groups[group].name, 'days': ["" for _ in range(40)],
                     'periods': ["" for _ in range(40)], 'subjects': ["" for _ in range(40)],
                     'rooms': ["" for _ in range(40)], 'teachers': ["" for _ in range(40)]}
        for period in range(len(periods)):
            for assignment in range(len(periods[period]['assignments'])):
                if periods[period]['assignments'][assignment].name == simple_groups[group].name:
                    timetable['days'][period] = periods[period]['day']
                    timetable['periods'][period] = periods[period]['period']
                    timetable['subjects'][period] = periods[period]['assignments'][assignment].subject
                    timetable['rooms'][period] = periods[period]['assignments'][assignment].room
                    timetable['teachers'][period] = periods[period]['assignments'][assignment].teacher
                    break
                if assignment == len(periods[period]['assignments']) - 1:
                    timetable['days'][period] = periods[period]['day']
                    timetable['periods'][period] = periods[period]['period']
        group_timetables.append(timetable)

    teacher_timetables = []
    for teacher in range(len(teachers)):
        timetable = {'name': teachers[teacher].name, 'days': ["" for _ in range(40)],
                     'periods': ["" for _ in range(40)], 'subjects': ["" for _ in range(40)],
                     'rooms': ["" for _ in range(40)], 'groups': ["" for _ in range(40)]}
        for period in range(len(periods)):
            for assignment in range(len(periods[period]['assignments'])):
                if periods[period]['assignments'][assignment].teacher == teachers[teacher].name:
                    timetable['days'][period] = periods[period]['day']
                    timetable['periods'][period] = periods[period]['period']
                    timetable['subjects'][period] = periods[period]['assignments'][assignment].subject
                    timetable['rooms'][period] = periods[period]['assignments'][assignment].room
                    timetable['groups'][period] = periods[period]['assignments'][assignment].name
                    break
                if assignment == len(periods[period]['assignments']):
                    timetable['days'][period] = periods[period]['day']
                    timetable['periods'][period] = periods[period]['period']
        teacher_timetables.append(timetable)

    room_timetables = []
    for room in range(len(rooms)):
        timetable = {'name': rooms[room].name, 'days': ["" for _ in range(40)],
                     'periods': ["" for _ in range(40)], 'subjects': ["" for _ in range(40)],
                     'teachers': ["" for _ in range(40)], 'groups': ["" for _ in range(40)]}
        for period in range(len(periods)):
            for assignment in range(len(periods[period]['assignments'])):
                if periods[period]['assignments'][assignment].room == rooms[room].name:
                    timetable['days'][period] = periods[period]['day']
                    timetable['periods'][period] = periods[period]['period']
                    timetable['subjects'][period] = periods[period]['assignments'][assignment].subject
                    timetable['teachers'][period] = periods[period]['assignments'][assignment].teacher
                    timetable['groups'][period] = periods[period]['assignments'][assignment].name
                    break
                if assignment == len(periods[period]['assignments']):
                    timetable['days'][period] = periods[period]['day']
                    timetable['periods'][period] = periods[period]['period']
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
        for period in range(len(time_windows[day])):
            for assignment in range(len(timetable['periods'])):
                if timetable['periods'][assignment] == time_windows[day][period] and\
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
                    break


def sortTeacherTimetable(timetable):
    counter = 0
    for day in time_windows.keys():
        for period in range(len(time_windows[day])):
            for assignment in range(len(timetable['periods'])):
                if timetable['periods'][assignment] == time_windows[day][period] and\
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
                    break


def sortRoomTimetable(timetable):
    counter = 0
    for day in time_windows.keys():
        for period in range(len(time_windows[day])):
            for assignment in range(len(timetable['periods'])):
                if timetable['periods'][assignment] == time_windows[day][period] and \
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
                    break

