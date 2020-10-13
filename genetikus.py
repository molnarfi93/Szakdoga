import data_loader
import random

NUM_TIME_WINDOWS = 30
SIZE_POPULATION = 100
NUM_GENERATIONS = 100
MUTATION_RATE = 5

classes = data_loader.load_classes(r'C:\Users\Brendi\Documents\Szakdoga\osztalyok.csv')
rooms = data_loader.load_rooms(r'C:\Users\Brendi\Documents\Szakdoga\tantermek.csv')
teachers = data_loader.load_teachers(r'C:\Users\Brendi\Documents\Szakdoga\tanarok.csv')
NUM_CLASSES = len(classes)
NUM_ROOMS = len(rooms)
NUM_TEACHERS = len(teachers)
if NUM_TEACHERS < NUM_ROOMS:
    MAX_PERIODS = NUM_TEACHERS
else:
    MAX_PERIODS = NUM_ROOMS

def getRandomGen():
    gen = []
    seated_rooms = []
    seated_teachers = []
    seated_classes = []
    for i in range(MAX_PERIODS):
        for j in range(NUM_CLASSES):
            if classes[j].sum_periods == 0:
                while True:
                    room = rooms[random.randint(0, NUM_ROOMS - 1)]
                    teacher = teachers[random.randint(0, NUM_TEACHERS - 1)]
                    if classes[j].headcount <= room.capacity:
                        if (classes[j].subject == teacher.either_subject or classes[j].subject == teacher.other_subject) and (teacher.sum_periods < teacher.weekly_periods):
                            break
                boole = True
                for k in range(len(seated_classes)):
                    if (classes[j].type != seated_classes[k].type) and (classes[j].grade == seated_classes[k].grade):
                        boole = False
                        break
                for k in range(len(seated_rooms)):
                    if room == seated_rooms[k]:
                        boole = False
                        break
                for k in range(len(seated_teachers)):
                    if teacher == seated_teachers[k]:
                        boole = False
                        break
                if boole:
                    seated_classes.append(classes[j])
                    seated_rooms.append(room)
                    seated_teachers.append(teacher)
                    classes[j].room = room.name
                    classes[j].teacher = teacher.name
                    classes[j].sum_periods += 1
                    teacher.sum_periods += 1
                    gen.append(classes[j])
                    break
    return gen


def calcError(entity):
    error = 0
    itemized = 0
    for i in range(NUM_TIME_WINDOWS):
        for j in range(len(entity['gens'][i])):
            if classes[entity['gens'][i][j].no].sum_periods == 0:
                itemized += 1
            classes[entity['gens'][i][j].no].sum_periods += 1
            error += classes[entity['gens'][i][j].no].sum_periods - 1
    error += NUM_CLASSES - itemized
    return error


entities = []
for i in range(SIZE_POPULATION):
    print(i)
    gens = []
    for j in range(NUM_TIME_WINDOWS):
        gens.append(getRandomGen())
    for j in range(NUM_CLASSES):
        classes[j].sum_periods = 0
    for j in range(NUM_TEACHERS):
        teachers[j].sum_periods = 0
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

best_entity = entities[SIZE_POPULATION - 1]
for i in range(NUM_TIME_WINDOWS):
    for j in range(len(best_entity['gens'][i])):
        print(best_entity['gens'][i][j].name, best_entity['gens'][i][j].subject, best_entity['gens'][i][j].room, best_entity['gens'][i][j].teacher)
    print("*****************************************")




