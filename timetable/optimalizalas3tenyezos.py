from optimalizalas2tenyezos import classes, NUM_CLASSES
import data_loader

teachers = data_loader.load_teachers(r'C:\Users\Brendi\Documents\Szakdoga\tanarok.json')
NUM_TEACHERS = len(teachers)

pairings = [[] for _ in range(len(classes))]
for i in range(NUM_CLASSES):
    for j in range(NUM_TEACHERS):
        for k in range(len(teachers[j].subjects)):
            if classes[i].subject == teachers[j].subjects[k]:
                pairings[i].append(1)
            else:
                pairings[i].append(0)

sum_periods = []
for i in range(NUM_TEACHERS):
    sum_periods.append(0)

for i in range(NUM_CLASSES):
    for j in range(NUM_TEACHERS):
        boole = False
        if pairings[i][j] == 1:
            for k in range(j, NUM_TEACHERS):
                if (sum_periods[k] < sum_periods[j]) & (pairings[i][k] == 1):
                    boole = True
            if not boole:
                classes[i].teacher = teachers[j].name
                sum_periods[j] += classes[i].weekly_periods
                break

for i in range(NUM_CLASSES):
    print(classes[i].name, classes[i].subject, classes[i].teacher)



