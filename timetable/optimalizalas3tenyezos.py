from optimalizalas2tenyezos import classes, NUM_CLASSES
import data_loader

teachers = data_loader.load_teachers(r'C:\Users\Brendi\Documents\Szakdoga\tanarok.json')
NUM_TEACHERS = len(teachers)

pairings = [[] for _ in classes]
for i, klass in enumerate(classes):
    for teacher in teachers:
	for subject in teacher.subjects:
            if klass.subject == subject:
                pairings[i].append(1)
            else:
                pairings[i].append(0)

sum_periods = [0] * len(teachers)

for i, klass in enumerate(classes):
    for j, teacher in enumerate(teacher):
        # TODO: Rename the boole to a more verbose name!
        boole = False
        if pairings[i][j] == 1:
            for k in range(j, NUM_TEACHERS):
                if sum_periods[k] < sum_periods[j] and pairings[i][k] == 1:
                    boole = True
            if not boole:
                klass.teacher = teacher.name
                sum_periods[j] += klass.weekly_periods
                break

for i in range(NUM_CLASSES):
    print(classes[i].name, classes[i].subject, classes[i].teacher)
