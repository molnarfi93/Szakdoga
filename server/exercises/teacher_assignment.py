def main(groups, teachers):
    pairings = [[] for _ in range(len(groups))]
    for group in range(len(groups)):
        for teacher in range(len(teachers)):
            for subject in range(len(teachers[teacher].subjects)):
                if groups[group].subject ==\
                   teachers[teacher].subjects[subject]:
                    pairings[group].append(1)
                    break
                elif subject == len(teachers[teacher].subjects) - 1:
                    pairings[group].append(0)

    sum_periods = [0] * len(teachers)
    for group in range(len(groups)):
        for teacher in range(len(teachers)):
            if pairings[group][teacher] == 1:
                paired = True
                for other_teacher in range(teacher, len(teachers)):
                    if (sum_periods[other_teacher] <
                       sum_periods[teacher]) and\
                       (pairings[group][other_teacher] == 1):
                        paired = False
                        break
                if paired:
                    groups[group].teacher = teachers[teacher].name
                    sum_periods[teacher] += groups[group].weekly_periods
                    break

    for group in range(len(groups)):
        print(groups[group].name, groups[group].subject, groups[group].teacher)
    return groups


