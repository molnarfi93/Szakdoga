from optimalizalas2tenyezos import groups, NUM_GROUPS
import data_loader

teachers = data_loader.load_teachers(r'C:\Users\Brendi\Documents\Szakdoga\tanarok.json')
NUM_TEACHERS = len(teachers)

pairings = [[] for _ in range(len(groups))]
for group in range(NUM_GROUPS):
    for teacher in range(NUM_TEACHERS):
        for subject in range(len(teachers[teacher].subjects)):
            if groups[group].subject == teachers[teacher].subjects[subject]:
                pairings[group].append(1)
            else:
                pairings[group].append(0)

sum_periods = [0] * len(teachers)
for group in range(NUM_GROUPS):
    for teacher in range(NUM_TEACHERS):
        paired = False
        if pairings[group][teacher] == 1:
            for other_teacher in range(teacher, NUM_TEACHERS):
                if (sum_periods[other_teacher] < sum_periods[teacher]) & (pairings[group][other_teacher] == 1):
                    paired = True
            if not paired:
                groups[group].teacher = teachers[teacher].name
                sum_periods[teacher] += groups[group].weekly_periods
                break

for group in range(NUM_GROUPS):
    print(groups[group].name, groups[group].subject, groups[group].teacher)
