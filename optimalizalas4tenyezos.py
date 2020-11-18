from optimalizalas3tenyezos import groups, teachers
import random

NUM_TIME_WINDOWS = 45
MAX_PERIODS = len(teachers)


sum_periods = [0] * len(groups)
def getPeriod():
    period = []
    seated_groups = []
    viewed_groups = []
    for _ in range(MAX_PERIODS):
        while True:
            if len(viewed_groups) == len(groups):
                return period
            rand = random.randint(0, len(groups) - 1)
            rand_group = groups[rand]
            ok = False
            for viewed_group in range(len(viewed_groups)):
                if rand == viewed_groups[viewed_group]:
                    ok = True
                    break
            if not ok:
                viewed_groups.append(rand)
                if sum_periods[rand] < rand_group.weekly_periods:
                    ok = True
                    for seated_group in range(len(seated_groups)):
                        if (rand_group.name == seated_groups[seated_group].name) or (rand_group.grade == seated_groups[seated_group].grade and rand_group.type != seated_groups[seated_group].type):
                            ok = False
                            break
                        elif rand_group.room == seated_groups[seated_group].room:
                            ok = False
                            break
                        elif rand_group.teacher == seated_groups[seated_group].teacher:
                            ok = False
                            break
                    if ok:
                        seated_groups.append(rand_group)
                        sum_periods[rand] += 1
                        period.append(rand_group)
                        break
    return period


periods = []
for period in range(NUM_TIME_WINDOWS):
    periods.append(getPeriod())
    for assignment in range(len(periods[period])):
        print(periods[period][assignment].name, periods[period][assignment].subject, periods[period][assignment].teacher, periods[period][assignment].room)
    print("************************************************")
