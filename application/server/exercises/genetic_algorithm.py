from enum import Enum
import random
import math

SIZE_POPULATION = 100
CROSSOVER_RATE = 80
MUTATION_RATE = 5
SCALE_MAX = 5
time_windows = {'m': [], 'tu': [], 'w': [], 'th': [], 'f': []}


class Day(Enum):
    m = 0
    tu = 1
    w = 2
    th = 3
    f = 4


def main(teachers, periods, timetable_datas):
    if timetable_datas['type'] == "college/university":
        DAILY_PERIODS = int((timetable_datas['end_time'] - timetable_datas['begin_time']) / 2)
    else:
        DAILY_PERIODS = timetable_datas['end_time'] - timetable_datas['begin_time']
    WEEKLY_PERIODS = DAILY_PERIODS * 5

    for day in range(5):
        day = Day(day)
        counter = timetable_datas['begin_time']
        for period in range(DAILY_PERIODS):
            time_windows[day.name].append(counter)
            if timetable_datas['type'] == "college/university":
                counter += 2
            else:
                counter += 1

    entities = []
    for entity in range(SIZE_POPULATION):
        gens = getRandomGens(WEEKLY_PERIODS)
        entities.append({'gens': gens, 'diff': 0, 'id': entity})
        entities[entity]['diff'] = targetFunction(entities[entity], teachers, periods, WEEKLY_PERIODS)

    total = 0
    counter = 0
    weights = [[] for _ in range(SIZE_POPULATION)]
    for entity in range(SIZE_POPULATION):
        total += entity
        for weight in range(counter, total):
            weights[entity].append(weight)
        counter = total

    while True:
        new_entities = []
        for entity in range(SIZE_POPULATION):
            new_entities.append(createChildren(entity, entities, teachers, periods, total, weights, WEEKLY_PERIODS))
        entities = new_entities
        sortEntities(entities)
        if entities[0]['diff'] - entities[SIZE_POPULATION - 1]['diff'] == 0:
            break

    for gen in range(WEEKLY_PERIODS):
        periods[gen]['day'] = entities[0]['gens']['days'][gen]
        periods[gen]['period'] = entities[0]['gens']['periods'][gen]

    return periods


def getRandomGens(WEEKLY_PERIODS):
    gens = {'days': [], 'periods': []}
    seated_windows = {'days': [], 'periods': []}
    for gen in range(WEEKLY_PERIODS):
        ok = False
        rand_day = math.nan
        rand_period = math.nan
        while not ok:
            ok = True
            rand_day = random.randint(0, 4)
            rand_day = Day(rand_day)
            rand_period =\
                time_windows[rand_day.name][random.randint(0,
                WEEKLY_PERIODS / 5 - 1)]
            for seated_window in range(len(seated_windows['days'])):
                if (rand_day.name ==
                   seated_windows['days'][seated_window]) and\
                   (rand_period ==
                   seated_windows['periods'][seated_window]):
                    ok = False
                    break
        gens['days'].append(rand_day.name)
        gens['periods'].append(rand_period)
        seated_windows['days'].append(rand_day.name)
        seated_windows['periods'].append(rand_period)
    return gens


def targetFunction(entity, teachers, periods, WEEKLY_PERIODS):
    diff = 0
    for teacher in range(len(teachers)):
        for period in range(WEEKLY_PERIODS):
            for assignment in range(len(periods[period]['assignments'])):
                if periods[period]['assignments'][assignment].teacher ==\
                   teachers[teacher].name:
                    if (entity['gens']['periods'][period] <
                       teachers[teacher].begin_time) or\
                       (entity['gens']['periods'][period] >
                       teachers[teacher].end_time):
                        diff += SCALE_MAX * 2
                    if entity['gens']['days'][period] == "f":
                        diff += teachers[teacher].balance *\
                            len(periods[period]) * 2
                    if entity['gens']['periods'][period] ==\
                       time_windows['f'][0]:
                        diff += (SCALE_MAX -
                            teachers[teacher].extremisms + 1) *\
                            len(periods[period]) * 2
                    elif entity['gens']['periods'][period] ==\
                       time_windows['f'][1]:
                        diff += (SCALE_MAX -
                            teachers[teacher].extremisms + 1) *\
                            len(periods[period])
                    elif entity['gens']['periods'][period] ==\
                       time_windows['f'][int(WEEKLY_PERIODS / 5) - 1]:
                        diff += teachers[teacher].extremisms *\
                            len(periods[period]) * 2
                    elif entity['gens']['periods'][period] ==\
                       time_windows['f'][int(WEEKLY_PERIODS / 5) - 2]:
                        diff += teachers[teacher].extremisms *\
                            len(periods[period])
    return diff


def sortEntities(entities):
    i = 0
    while i < SIZE_POPULATION - 1:
        max = entities[i]
        maxindex = i
        j = i + 1
        while j < SIZE_POPULATION:
            if entities[j]['diff'] > max['diff']:
                max = entities[j]
                maxindex = j
            j += 1
        if maxindex != i:
            entities[maxindex] = entities[i]
            entities[i] = max
        i += 1


def createChildren(entity, entities, teachers, periods, total, weights, WEEKLY_PERIODS):
    either_parent = selectParent({'gens': {'days': [], 'periods': []},
                    'diff': 0, 'id': entity}, entities, total, weights)
    other_parent = selectParent(either_parent, entities, total, weights)
    order_crossover = random.randint(1, 100)
    if order_crossover > (100 - CROSSOVER_RATE):
        child = crossover(either_parent, other_parent, entity, WEEKLY_PERIODS)
    else:
        child = clear_inheritance(either_parent, entity, WEEKLY_PERIODS)
    order_mutation = random.randint(1, 100)
    if order_mutation > (100 - MUTATION_RATE):
        child = mutation(child, entities, WEEKLY_PERIODS)
    child['diff'] = targetFunction(child, teachers, periods, WEEKLY_PERIODS)
    return child


def selectParent(either_parent, entities, total, weights):
    while True:
        rand = random.randint(0, total - 1)
        for entity in range(SIZE_POPULATION):
            for weight in range(len(weights[entity])):
                if rand == weights[entity][weight]:
                    if entities[entity]['id'] != either_parent['id']:
                        return entities[entity]


def crossover(either_parent, other_parent, entity, WEEKLY_PERIODS):
    child = {'gens': {'days': [], 'periods': []},
             'diff': 0, 'id': entity}
    crossover_point = random.randint(0, WEEKLY_PERIODS - 1)
    for gen in range(0, crossover_point):
        child['gens']['days'].append(
            either_parent['gens']['days'][gen])
        child['gens']['periods'].append(
            either_parent['gens']['periods'][gen])
    for gen in range(crossover_point, WEEKLY_PERIODS):
        ok = True
        for child_gen in range(len(child['gens']['days'])):
            if (child['gens']['days'][child_gen] ==
               other_parent['gens']['days'][gen]) and\
               (child['gens']['periods'][child_gen] ==
               other_parent['gens']['periods'][gen]):
                ok = False
                break
        if ok:
            child['gens']['days'].append(
                other_parent['gens']['days'][gen])
            child['gens']['periods'].append(
                other_parent['gens']['periods'][gen])
        else:
            for parent_gen in range(0, crossover_point):
                ok = True
                for child_gen in range(len(child['gens']['days'])):
                    if (other_parent['gens']['days'][parent_gen] ==
                       child['gens']['days'][child_gen]) and\
                       (other_parent['gens']['periods'][parent_gen] ==
                       child['gens']['periods'][child_gen]):
                        ok = False
                        break
                if ok:
                    child['gens']['days'].append(
                        other_parent['gens']['days'][parent_gen])
                    child['gens']['periods'].append(
                        other_parent['gens']['periods'][parent_gen])
                    break
    return child


def clear_inheritance(either_parent, entity, WEEKLY_PERIODS):
    child = {'gens': {'days': [], 'periods': []},
             'diff': 0, 'id': entity}
    for gen in range(0, WEEKLY_PERIODS):
        child['gens']['days'].append(either_parent['gens']['days'][gen])
        child['gens']['periods'].append(
            either_parent['gens']['periods'][gen])
    return child


def mutation(child, entities, WEEKLY_PERIODS):
    rand_entity = entities[random.randint(0, SIZE_POPULATION - 1)]
    muted_gen = random.randint(0, WEEKLY_PERIODS - 1)
    for gen in range(0, WEEKLY_PERIODS - 1):
        if (child['gens']['days'][gen] ==
           rand_entity['gens']['days'][WEEKLY_PERIODS - 1]) and\
           (child['gens']['periods'][gen] ==
           rand_entity['gens']['periods'][WEEKLY_PERIODS - 1]):
            child['gens']['days'][gen] ==\
                child['gens']['days'][muted_gen]
            child['gens']['periods'][gen] ==\
                child['gens']['periods'][muted_gen]
            child['gens']['days'][muted_gen] ==\
                rand_entity['gens']['days'][WEEKLY_PERIODS - 1]
            child['gens']['periods'][muted_gen] ==\
                rand_entity['gens']['periods'][WEEKLY_PERIODS - 1]
            break
    return child






