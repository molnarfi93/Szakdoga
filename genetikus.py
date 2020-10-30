from optimalizalas3tenyezos import groups, teachers
from optimalizalas2tenyezos import rooms
import random

NUM_TIME_WINDOWS = 45
SIZE_POPULATION = 100
NUM_GENERATIONS = 100
MUTATION_RATE = 5
NUM_GROUPS = len(groups)
NUM_ROOMS = len(rooms)
NUM_TEACHERS = len(teachers)
MAX_PERIODS = NUM_TEACHERS


def getRandomGen(sum_periods):
    gen = []
    seated_groups = []
    viewed_groups = []
    for _ in range(MAX_PERIODS):
        while True:
            if len(viewed_groups) == NUM_GROUPS:
                return gen
            rand = groups[random.randint(0, NUM_GROUPS - 1)]
            ok = False
            for viewed_group in range(len(viewed_groups)):
                if rand.no == viewed_groups[viewed_group]:
                    ok = True
                    break
            if not ok:
                viewed_groups.append(rand.no)
                if sum_periods[rand.no] < rand.weekly_periods:
                    ok = True
                    for seated_group in range(len(seated_groups)):
                        if (rand.name == seated_groups[seated_group].name) or (rand.grade == seated_groups[seated_group].grade and rand.type != seated_groups[seated_group].type):
                            ok = False
                            break
                        elif rand.room == seated_groups[seated_group].room:
                            ok = False
                            break
                        elif rand.teacher == seated_groups[seated_group].teacher:
                            ok = False
                            break
                    if ok:
                        seated_groups.append(rand)
                        sum_periods[rand.no] += 1
                        gen.append(rand)
                        break


def calcError(entity):
    error = 0
    sum_periods = [0] * len(groups)
    for period in range(NUM_TIME_WINDOWS):
        for assignment in range(len(entity['gens'][period])):
            sum_periods[entity['gens'][period][assignment].no] += 1
    for group in range(NUM_GROUPS):
        error += abs(sum_periods[group] - groups[group].weekly_periods)
    return error


entities = []
for entity in range(SIZE_POPULATION):
    print(entity)
    gens = []
    sum_periods = [0] * len(groups)
    for _ in range(NUM_TIME_WINDOWS):
        gens.append(getRandomGen(sum_periods))
    entities.append({'gens': gens, 'error': 0, 'id': entity})


def sortEntities():
    i = 0
    while i < SIZE_POPULATION - 1:
        max = entities[i]
        maxindex = i
        j = i + 1
        while j < SIZE_POPULATION:
            if entities[j]['error'] > max['error']:
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


def createChildren(entity):
    either_parent = selectParent({'gens': [], 'error': 0, 'id': entity})
    other_parent = selectParent(either_parent)
    child = {'gens': [], 'error': 0, 'id': entity}
    crossover_point = random.randint(0, NUM_TIME_WINDOWS)
    for gen in range(crossover_point):
        child['gens'].append(either_parent['gens'][gen])
    for gen in range(crossover_point, NUM_TIME_WINDOWS):
        child['gens'].append(other_parent['gens'][gen])
    mutation = random.randint(1, 100)
    if mutation > 100 - MUTATION_RATE:
        randentity = random.randint(0, SIZE_POPULATION - 1)
        muted_gen = random.randint(0, NUM_TIME_WINDOWS - 1)
        tmp = entities[randentity]['gens'][NUM_TIME_WINDOWS - 1]
        entities[randentity]['gens'][NUM_TIME_WINDOWS - 1] = child['gens'][muted_gen]
        child['gens'][muted_gen] = tmp
    child['error'] = calcError(child)
    return child


for _ in range(NUM_GENERATIONS):
    new_entities = []
    for entity in range(SIZE_POPULATION):
        new_entities.append(createChildren(entity))
    entities = new_entities
    sortEntities()
for entity in range (len(entities)):
    print(entities[entity]['error'])

best_entity = entities[SIZE_POPULATION - 1]
for period in range(NUM_TIME_WINDOWS):
    for assignment in range(len(best_entity['gens'][period])):
        print(best_entity['gens'][period][assignment].name, best_entity['gens'][period][assignment].subject, best_entity['gens'][period][assignment].room, best_entity['gens'][period][assignment].teacher)
    print("*****************************************")




