from optimalizalas3tenyezos import classes, NUM_CLASSES, NUM_TEACHERS
from optimalizalas2tenyezos import NUM_ROOMS

NUM_TIME_WINDOWS = 45
if NUM_TEACHERS < NUM_ROOMS:
    MAX_PERIODS = NUM_TEACHERS
else:
    MAX_PERIODS = NUM_ROOMS


def getTimetable():
    timetable = []
    seated_classes = []
    seated_rooms = []
    seated_teachers = []
    for i in range(MAX_PERIODS):
        for j in range(NUM_CLASSES):
            if classes[j].sum_periods < classes[j].weekly_periods:
                boole = True
                for k in range(len(seated_classes)):
                    if (classes[j].name == seated_classes[k].name) or (classes[j].grade == seated_classes[k].grade and classes[j].type != seated_classes[k].type):
                        boole = False
                        break
                for k in range(len(seated_rooms)):
                    if classes[j].room == seated_rooms[k]:
                        boole = False
                        break
                for k in range(len(seated_teachers)):
                    if classes[j].teacher == seated_teachers[k]:
                        boole = False
                        break
                if boole:
                    seated_classes.append(classes[j])
                    seated_rooms.append(classes[j].room)
                    seated_teachers.append(classes[j].teacher)
                    classes[j].sum_periods += 1
                    timetable.append(classes[j])
                    break
    return timetable


timetables = []
for i in range(NUM_TIME_WINDOWS):
    print(i)
    timetables.append(getTimetable())
    for j in range(len(timetables[i])):
        print(timetables[i][j].name, timetables[i][j].subject, timetables[i][j].teacher, timetables[i][j].room)
    print("************************************************")
