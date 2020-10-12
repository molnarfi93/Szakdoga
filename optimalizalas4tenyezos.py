from optimalizalas2tenyezos import classes, NUM_CLASSES
NUM_TIME_WINDOWS = 36
def getTimetable():
    timetable = []
    seated_classes = []
    seated_rooms = []
    seated_teachers = []
    for i in range (20):
        for j in range (NUM_CLASSES):
            if classes[j].sum_periods < classes[j].weekly_periods:
                boole = True
                for k in range(len(seated_classes)):
                    if (classes[j].name == seated_classes[k].name) or (classes[j].grade == seated_classes[k].grade and classes[j].type != seated_classes[k].type):
                        boole = False
                for k in range(len(seated_rooms)):
                    if classes[j].room == seated_rooms[k]:
                        boole = False
                for k in range(len(seated_teachers)):
                    if classes[j].teacher == seated_teachers[k]:
                        boole = False
                if boole:
                    seated_classes.append(classes[j])
                    seated_rooms.append(classes[j].room)
                    seated_teachers.append(classes[j].teacher)
                    classes[j].sum_periods += 1
                    timetable.append(classes[j].name, classes[j].subject, classes[j].teacher, classes[j].room)
                    break
    return timetable
timetables = []
for i in range (NUM_TIME_WINDOWS):
    timetables.append(getTimetable())
    print(timetables[i])
