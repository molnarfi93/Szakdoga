import exercises.room_assignment
import exercises.teacher_assignment
import exercises.window_classification
import exercises.genetic_algorithm as genetic_algorithm
import exporter

time_windows = genetic_algorithm.time_windows


def generateTimetables(timetable_datas, rooms, teachers, simple_groups):
    if timetable_datas['type'] == "college/university":
        WEEKLY_PERIODS = int((timetable_datas['end_time'] - timetable_datas['begin_time']) / 2) * 5
    else:
        WEEKLY_PERIODS = (timetable_datas['end_time'] - timetable_datas['begin_time']) * 5

    groups = room_assignment.main(simple_groups, rooms)
    if timetable_datas['add_manually'] is False:
        groups = teacher_assignment.main(groups, teachers)
    periods = window_classification.main(groups, teachers)
    periods = genetic_algorithm.main(teachers, periods, timetable_datas)

    group_timetables = []
    for group in range(len(simple_groups)):
        timetable = {'name': simple_groups[group].name, 'days': ["" for _ in range(WEEKLY_PERIODS)],
                     'periods': ["" for _ in range(WEEKLY_PERIODS)], 'subjects': ["" for _ in range(WEEKLY_PERIODS)],
                     'rooms': ["" for _ in range(WEEKLY_PERIODS)], 'teachers': ["" for _ in range(WEEKLY_PERIODS)]}
        for period in range(len(periods)):
            found = False
            for assignment in range(len(periods[period]['assignments'])):
                if periods[period]['assignments'][assignment].name == simple_groups[group].name:
                    timetable['days'][period] = periods[period]['day']
                    timetable['periods'][period] = periods[period]['period']
                    timetable['subjects'][period] = periods[period]['assignments'][assignment].subject
                    timetable['rooms'][period] = periods[period]['assignments'][assignment].room
                    timetable['teachers'][period] = periods[period]['assignments'][assignment].teacher
                    found = True
                    break
            if found is False:
                timetable['days'][period] = periods[period]['day']
                timetable['periods'][period] = periods[period]['period']
        group_timetables.append(timetable)

    teacher_timetables = []
    for teacher in range(len(teachers)):
        timetable = {'name': teachers[teacher].name, 'days': ["" for _ in range(WEEKLY_PERIODS)],
                     'periods': ["" for _ in range(WEEKLY_PERIODS)], 'subjects': ["" for _ in range(WEEKLY_PERIODS)],
                     'rooms': ["" for _ in range(WEEKLY_PERIODS)], 'groups': ["" for _ in range(WEEKLY_PERIODS)]}
        for period in range(len(periods)):
            found = False
            for assignment in range(len(periods[period]['assignments'])):
                if periods[period]['assignments'][assignment].teacher == teachers[teacher].name:
                    timetable['days'][period] = periods[period]['day']
                    timetable['periods'][period] = periods[period]['period']
                    timetable['subjects'][period] = periods[period]['assignments'][assignment].subject
                    timetable['rooms'][period] = periods[period]['assignments'][assignment].room
                    timetable['groups'][period] = periods[period]['assignments'][assignment].name
                    found = True
                    break
            if found is False:
                timetable['days'][period] = periods[period]['day']
                timetable['periods'][period] = periods[period]['period']
        teacher_timetables.append(timetable)

    room_timetables = []
    for room in range(len(rooms)):
        timetable = {'name': rooms[room].name, 'days': ["" for _ in range(WEEKLY_PERIODS)],
                     'periods': ["" for _ in range(WEEKLY_PERIODS)], 'subjects': ["" for _ in range(WEEKLY_PERIODS)],
                     'teachers': ["" for _ in range(WEEKLY_PERIODS)], 'groups': ["" for _ in range(WEEKLY_PERIODS)]}
        for period in range(len(periods)):
            found = False
            for assignment in range(len(periods[period]['assignments'])):
                if periods[period]['assignments'][assignment].room == rooms[room].name:
                    timetable['days'][period] = periods[period]['day']
                    timetable['periods'][period] = periods[period]['period']
                    timetable['subjects'][period] = periods[period]['assignments'][assignment].subject
                    timetable['teachers'][period] = periods[period]['assignments'][assignment].teacher
                    timetable['groups'][period] = periods[period]['assignments'][assignment].name
                    found = True
                    break
            if found is False:
                timetable['days'][period] = periods[period]['day']
                timetable['periods'][period] = periods[period]['period']
        room_timetables.append(timetable)

    for timetable in range(len(group_timetables)):
        sortGroupTimetable(group_timetables[timetable])
    for timetable in range(len(teacher_timetables)):
        sortTeacherTimetable(teacher_timetables[timetable])
    for timetable in range(len(room_timetables)):
        sortRoomTimetable(room_timetables[timetable])

    if timetable_datas['type'] == 'college/university':
        double_periods = True
    else:
        double_periods = False
    exporter.exportTimetables(group_timetables, teacher_timetables, room_timetables, double_periods)


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

