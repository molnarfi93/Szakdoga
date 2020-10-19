import data_loader
from optimalizalas3tenyezos import classes
import random

NUM_TIME_WINDOWS = 45
SIZE_POPULATION = 100
NUM_GENERATIONS = 100
MUTATION_RATE = 5

rooms = data_loader.load_rooms(r'tantermek.csv')
teachers = data_loader.load_teachers(r'tanarok.csv')
NUM_CLASSES = len(classes)
NUM_ROOMS = len(rooms)
NUM_TEACHERS = len(teachers)
MAX_PERIODS = NUM_TEACHERS


def getRandomGen():
    gen = []
    seated_classes = []
    viewed_classes = []
    for i in range(MAX_PERIODS):
        while True:
            if len(viewed_classes) == NUM_CLASSES:
                return gen
            rand = classes[random.randint(0, NUM_CLASSES - 1)]
            boole = False
            for k in range(len(viewed_classes)):
                if rand.no == viewed_classes[k]:
                    boole = True
                    break
            if not boole:
                viewed_classes.append(rand.no)
                if rand.sum_periods < rand.weekly_periods:
                    found = True
                    for k in range(len(seated_classes)):
                        if (rand.name == seated_classes[k].name) or (rand.grade == seated_classes[k].grade and rand.type != seated_classes[k].type):
                            found = False
                            break
                        elif rand.room == seated_classes[k].room:
                            found = False
                            break
                        elif rand.teacher == seated_classes[k].teacher:
                            found = False
                            break
                    if found:
                        seated_classes.append(rand)
                        classes[rand.no].sum_periods += 1
                        gen.append(rand)
                        break


def calcError(entity):
    error = 0
    for i in range(NUM_TIME_WINDOWS):
        for j in range(len(entity['gens'][i])):
            classes[entity['gens'][i][j].no].sum_periods += 1
    for i in range(NUM_CLASSES):
        error += abs(classes[i].sum_periods - classes[i].weekly_periods)
    return error


entities = []
for i in range(SIZE_POPULATION):
    print(i)
    gens = []
    for j in range(NUM_TIME_WINDOWS):
        gens.append(getRandomGen())
    for j in range(NUM_CLASSES):
        classes[j].sum_periods = 0
    entities.append({'gens': gens, 'error': 0, 'id': i})


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
for i in range(SIZE_POPULATION):
    total += i
    for j in range(counter, total):
        weights[i].append(j)
    counter = total


def selectParent(either_parent):
    while True:
        rand = random.randint(0, total - 1)
        for i in range(SIZE_POPULATION):
            for j in range(len(weights[i])):
                if rand == weights[i][j]:
                    if entities[i]['id'] != either_parent['id']:
                        return entities[i]


def createChildren(j):
    either_parent = selectParent({'gens': [], 'error': 0, 'id': j})
    other_parent = selectParent(either_parent)
    child = {'gens': [], 'error': 0, 'id': j}
    crossover_point = random.randint(0, NUM_TIME_WINDOWS)
    for i in range(crossover_point):
        child['gens'].append(either_parent['gens'][i])
    for i in range(crossover_point, NUM_TIME_WINDOWS):
        child['gens'].append(other_parent['gens'][i])
    mutation = random.randint(1, 100)
    if mutation > 100 - MUTATION_RATE:
        randomentity = random.randint(0, SIZE_POPULATION - 1)
        muted_gen = random.randint(0, NUM_TIME_WINDOWS - 1)
        tmp = entities[randomentity]['gens'][NUM_TIME_WINDOWS - 1]
        entities[randomentity]['gens'][NUM_TIME_WINDOWS - 1] = child['gens'][muted_gen]
        child['gens'][muted_gen] = tmp
    child['error'] = calcError(child)
    for i in range(NUM_CLASSES):
        classes[i].sum_periods = 0
    return child


for i in range(NUM_GENERATIONS):
    new_entities = []
    for j in range(SIZE_POPULATION):
        new_entities.append(createChildren(j))
    entities = new_entities
    sortEntities()
for i in range (len(entities)):
    print(entities[i]['error'])

best_entity = entities[SIZE_POPULATION - 1]
for i in range(NUM_TIME_WINDOWS):
    for j in range(len(best_entity['gens'][i])):
        print(best_entity['gens'][i][j].name, best_entity['gens'][i][j].subject, best_entity['gens'][i][j].room, best_entity['gens'][i][j].teacher)
    print("*****************************************")




