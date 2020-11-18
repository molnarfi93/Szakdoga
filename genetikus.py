from optimalizalas3tenyezos import teachers
from optimalizalas4tenyezos import periods
from enum import Enum
import random
import math

SIZE_POPULATION = 100
CROSSOVER_RATE = 80
MUTATION_RATE = 5
SCALE_MAX = 5
MAX_PERIODS = len(teachers)
DAILY_PERIODS = 9
NUM_GENS = DAILY_PERIODS * 5
time_windows = {'m': ["7-8", "8-9", "9-10", "10-11", "11-12", "12-13", "13-14", "14-15", "15-16"],
                'tu': ["7-8", "8-9", "9-10", "10-11", "11-12", "12-13", "13-14", "14-15", "15-16"],
                'w': ["7-8", "8-9", "9-10", "10-11", "11-12", "12-13", "13-14", "14-15", "15-16"],
                'th': ["7-8", "8-9", "9-10", "10-11", "11-12", "12-13", "13-14", "14-15", "15-16"],
                'f': ["7-8", "8-9", "9-10", "10-11", "11-12", "12-13", "13-14", "14-15", "15-16"]}


class Day(Enum):
    m = 0
    tu = 1
    w = 2
    th = 3
    f = 4


def getRandomGens():
    gens = {'days': [], 'periods': []}
    seated_windows = {'days': [], 'periods': []}
    for gen in range(NUM_GENS):
        ok = False
        rand_day = math.nan
        rand_period = math.nan
        while not ok:
            ok = True
            rand_day = random.randint(0, 4)
            rand_day = Day(rand_day)
            rand_period = time_windows[rand_day.name][random.randint(0, DAILY_PERIODS - 1)]
            for seated_window in range(len(seated_windows['days'])):
                if (rand_day.name == seated_windows['days'][seated_window]) and (rand_period == seated_windows['periods'][seated_window]):
                    ok = False
                    break
        gens['days'].append(rand_day.name)
        gens['periods'].append(rand_period)
        seated_windows['days'].append(rand_day.name)
        seated_windows['periods'].append(rand_period)
    return gens


def targetFunction(entity):
    diff = 0
    for teacher in range(len(teachers)):
        for gen in range(NUM_GENS):
            if entity['gens']['days'][gen] == "f":
                diff += teachers[teacher].balance * len(periods[gen])
            else:
                diff += (SCALE_MAX - teachers[teacher].balance + 1) * len(periods[gen])
            if entity['gens']['periods'][gen] == time_windows['f'][0]:
                diff += (SCALE_MAX - teachers[teacher].extremisms + 1) * len(periods[gen]) * 2
            elif entity['gens']['periods'][gen] == time_windows['f'][1]:
                diff += (SCALE_MAX - teachers[teacher].extremisms + 1) * len(periods[gen])
            elif entity['gens']['periods'][gen] == time_windows['f'][DAILY_PERIODS - 1]:
                diff += teachers[teacher].extremisms * len(periods[gen]) * 2
            elif entity['gens']['periods'][gen] == time_windows['f'][DAILY_PERIODS - 2]:
                diff += teachers[teacher].extremisms * len(periods[gen])
    return diff


entities = []
for entity in range(SIZE_POPULATION):
    gens = getRandomGens()
    entities.append({'gens': gens, 'diff': 0, 'id': entity})
    entities[entity]['diff'] = targetFunction(entities[entity])


def sortEntities():
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


total = 0
counter = 0
weights = [[] for _ in range(SIZE_POPULATION)]
for entity in range(SIZE_POPULATION):
    total += entity
    for weight in range(counter, total):
        weights[entity].append(weight)
    counter = total


def selectParent(either_parent):
    while True:
        rand = random.randint(0, total - 1)
        for entity in range(SIZE_POPULATION):
            for weight in range(len(weights[entity])):
                if rand == weights[entity][weight]:
                    if entities[entity]['id'] != either_parent['id']:
                        return entities[entity]


def crossover(either_parent, other_parent):
    child = {'gens': {'days': [], 'periods': []}, 'diff': 0, 'id': entity}
    crossover_point = random.randint(0, NUM_GENS - 1)
    for gen in range(0, crossover_point):
        child['gens']['days'].append(either_parent['gens']['days'][gen])
        child['gens']['periods'].append(either_parent['gens']['periods'][gen])
    for gen in range(crossover_point, NUM_GENS):
        ok = True
        for child_gen in range(len(child['gens']['days'])):
            if (child['gens']['days'][child_gen] == other_parent['gens']['days'][gen]) and (child['gens']['periods'][child_gen] == other_parent['gens']['periods'][gen]):
                ok = False
                break
        if ok:
            child['gens']['days'].append(other_parent['gens']['days'][gen])
            child['gens']['periods'].append(other_parent['gens']['periods'][gen])
        else:
            for parent_gen in range(0, crossover_point):
                ok = True
                for child_gen in range(len(child['gens']['days'])):
                    if (other_parent['gens']['days'][parent_gen] == child['gens']['days'][child_gen]) and (other_parent['gens']['periods'][parent_gen] == child['gens']['periods'][child_gen]):
                        ok = False
                        break
                if ok:
                    child['gens']['days'].append(other_parent['gens']['days'][parent_gen])
                    child['gens']['periods'].append(other_parent['gens']['periods'][parent_gen])
                    break
    return child


def clear_inheritance(either_parent):
    child = {'gens': {'days': [], 'periods': []}, 'diff': 0, 'id': entity}
    for gen in range(0, NUM_GENS):
        child['gens']['days'].append(either_parent['gens']['days'][gen])
        child['gens']['periods'].append(either_parent['gens']['periods'][gen])
    return child


def mutation(child):
    rand_entity = entities[random.randint(0, SIZE_POPULATION - 1)]
    muted_gen = random.randint(0, NUM_GENS - 1)
    for gen in range(0, NUM_GENS - 1):
        if (child['gens']['days'][gen] == rand_entity['gens']['days'][NUM_GENS - 1]) and (child['gens']['periods'][gen] == rand_entity['gens']['periods'][NUM_GENS - 1]):
            child['gens']['days'][gen] == child['gens']['days'][muted_gen]
            child['gens']['periods'][gen] == child['gens']['periods'][muted_gen]
            child['gens']['days'][muted_gen] == rand_entity['gens']['days'][NUM_GENS - 1]
            child['gens']['periods'][muted_gen] == rand_entity['gens']['periods'][NUM_GENS - 1]
            break
    return child


def createChildren(entity):
    either_parent = selectParent({'gens': {'days': [], 'periods': []}, 'diff': 0, 'id': entity})
    other_parent = selectParent(either_parent)
    order_crossover = random.randint(1, 100)
    if order_crossover > (100 - CROSSOVER_RATE):
        child = crossover(either_parent, other_parent)
    else:
        child = clear_inheritance(either_parent)
    order_mutation = random.randint(1, 100)
    if order_mutation > (100 - MUTATION_RATE):
        child = mutation(child)
    child['diff'] = targetFunction(child)
    return child


while True:
    new_entities = []
    for entity in range(SIZE_POPULATION):
        new_entities.append(createChildren(entity))
    entities = new_entities
    sortEntities()
    if entities[0]['diff'] - entities[SIZE_POPULATION - 1]['diff'] == 0:
        break

for day in range(len(time_windows)):
    day = Day(day)
    for period in range(len(time_windows['f'])):
        for gen in range(NUM_GENS):
            if (entities[0]['gens']['days'][gen] == day.name) and (entities[0]['gens']['periods'][gen] == time_windows[day.name][period]):
                print(entities[0]['gens']['days'][gen]+" "+entities[0]['gens']['periods'][gen])
                for assignment in range(len(periods[gen])):
                    print(periods[gen][assignment].name, periods[gen][assignment].subject, periods[gen][assignment].room, periods[gen][assignment].teacher)
                print("*****************************************")
                break



