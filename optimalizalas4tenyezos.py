from optimalizalas3tenyezos import classes, NUM_CLASSES, NUM_TEACHERS

NUM_TIME_WINDOWS = 45
MAX_PERIODS = NUM_TEACHERS


def getTimetable():
    timetable = []
    seated_classes = []
    for i in range(MAX_PERIODS):
        for j in range(NUM_CLASSES):
            if classes[j].sum_periods < classes[j].weekly_periods:
                boole = True
                for k in range(len(seated_classes)):
                    if (classes[j].name == seated_classes[k].name) or (classes[j].grade == seated_classes[k].grade and classes[j].type != seated_classes[k].type):
                        boole = False
                        break
                    elif classes[j].room == seated_classes[k].room:
                        boole = False
                        break
                    elif classes[j].teacher == seated_classes[k].teacher:
                        boole = False
                        break
                if boole:
                    seated_classes.append(classes[j])
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
