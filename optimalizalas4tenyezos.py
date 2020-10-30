from optimalizalas3tenyezos import groups, NUM_GROUPS, NUM_TEACHERS

NUM_TIME_WINDOWS = 45
MAX_PERIODS = NUM_TEACHERS


sum_periods = [0] * len(groups)
def getPeriod():
    period = []
    seated_groups = []
    for _ in range(MAX_PERIODS):
        for group in range(NUM_GROUPS):
            if sum_periods[group] < groups[group].weekly_periods:
                ok = True
                for seated_group in range(len(seated_groups)):
                    if (groups[group].name == seated_groups[seated_group].name) or (groups[group].grade == seated_groups[seated_group].grade and groups[group].type != seated_groups[seated_group].type):
                        ok = False
                        break
                    elif groups[group].room == seated_groups[seated_group].room:
                        ok = False
                        break
                    elif groups[group].teacher == seated_groups[seated_group].teacher:
                        ok = False
                        break
                if ok:
                    seated_groups.append(groups[group])
                    sum_periods[group] += 1
                    period.append(groups[group])
                    break
    return period


periods = []
for period in range(NUM_TIME_WINDOWS):
    periods.append(getPeriod())
    for assignment in range(len(periods[period])):
        print(periods[period][assignment].name, periods[period][assignment].subject, periods[period][assignment].teacher, periods[period][assignment].room)
    print("************************************************")
