from optimalizalas2tenyezos import classes, NUM_CLASSES
import data_loader

teachers = data_loader.load_teachers(r'tanarok.csv')
NUM_TEACHERS = len(teachers)

pairings = [[] for _ in range(len(classes))]
for i in range(NUM_CLASSES):
    for j in range(NUM_TEACHERS):
        if (classes[i].subject == teachers[j].either_subject) or (classes[i].subject == teachers[j].other_subject):
            pairings[i].append(1)
        else:
            pairings[i].append(0)

for i in range(NUM_CLASSES):
    for j in range(NUM_TEACHERS):
        boole = False
        if pairings[i][j] == 1:
            for k in range(j, NUM_TEACHERS):
                if (teachers[k].sum_periods < teachers[j].sum_periods) & (pairings[i][k] == 1):
                    boole = True
            if not boole:
                classes[i].teacher = teachers[j].name
                teachers[j].sum_periods += classes[i].weekly_periods
                break

for i in range(NUM_CLASSES):
    print(classes[i].name, classes[i].subject, classes[i].teacher)



