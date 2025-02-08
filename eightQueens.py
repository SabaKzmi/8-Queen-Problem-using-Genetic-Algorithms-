import random

# there are 4,426,165,368 possible arrangements (8x8)
# only 92 distinct solutions

def make_population(n):
    # index = row   and    value = column that has the queen
    pop = []
    for i in range(n):
        new_member = random.sample(range(8), 8)
        pop.append(new_member)
    return pop

def fitness(board):
    error = 0
    for row in range(8):
        for i in range(8):
            if i - row == 0: pass; #same row -> same queen
            elif abs(board[row] - board[i]) == abs(row - i):
                error += 1
    return 1/((error // 2) + 1) #the threat between two queens is calculated twice - the larger fitness the better

def choose_parents(pop):
    best_arrangement = None
    max_value = float('-inf')
    second_best_arrangement = None
    second_max_value = float('-inf')

    tournament_list = random.sample(pop, 3)
    for s in tournament_list:
        if fitness(s) > max_value:
            second_best_arrangement, second_max_value = best_arrangement, max_value
            best_arrangement = s
            max_value = fitness(s)
        elif second_max_value < fitness(s) <= max_value:
            second_best_arrangement = s
            second_max_value = fitness(s)
    return best_arrangement, second_best_arrangement

def find_multiple_elite(pop, num):
    pop_copy = pop.copy()
    elite = [None] * num
    for n in range(num):
        elite[n] = pop_copy[0]
        for c in pop_copy:
            if fitness(c) > fitness(elite[n]):
                elite[n] = c
        pop_copy.remove(elite[n])
    return elite

def find_elite(pop):
    elite = pop[0]
    for c in pop:
        if fitness(c) > fitness(elite):
            elite = c
    return elite

#ox crossover
def crossover(parent1, parent2):
    child1 = [None] * 8
    child2 = [None] * 8

    #choose points
    startPoint, endPoint = random.sample(range(8), 2)
    if endPoint < startPoint: startPoint, endPoint = endPoint, startPoint

    #copying the part in between two points to the child
    for i in range(startPoint, endPoint + 1):
        child1[i] = parent1[i]
        child2[i] = parent2[i]

    #completing the children
    #list of indexes that should be visited in parents
    index_list = list(range(endPoint + 1, len(parent1)))
    index_list += list(range(endPoint + 1))

    ch1_index , ch2_index = index_list, index_list
    i1, i2 = 0, 0
    #going through indexes
    for i in index_list:
        if parent2[i] not in child1:
            child1[ch1_index[i1]] = parent2[i]
            i1 += 1
        if parent1[i] not in child2:
            child2[ch2_index[i2]] = parent1[i]
            i2 += 1

    return child1, child2

def mutation(arrangement):
    firstPoint, secondPoint = random.sample(range(8), 2)
    arrangement[firstPoint], arrangement[secondPoint] = arrangement[secondPoint], arrangement[firstPoint]
    return arrangement

def print_board(board):
    tab = "     "
    queen = "  Q  "
    print("-------------------------------------------------")
    for r in range(8):
        s = [tab] * 8
        s[board[r]] = queen
        print("|{}|{}|{}|{}|{}|{}|{}|{}|".format(s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7]))
        print("-------------------------------------------------")

#---------- main ----------
population = make_population(100)
generation_num = 1

while generation_num < 500:
    e = find_multiple_elite(population, 2 * (len(population) // 10))
    newPopulation = [e[i] for i in range(len(e))]
    for i in range(8 * (len(population) // 10) // 2):
        p1, p2 = choose_parents(population)
        ch1, ch2 = crossover(p1, p2)
        newPopulation.append(mutation(ch1))
        newPopulation.append(mutation(ch2))
    generation_num += 1
    population = newPopulation

print("best fit: ", find_elite(population), "   fitness: ", fitness(find_elite(population)))

solution_count = 0
for a in population:
    if fitness(a) == 1:
        print("***************************************************")
        print_board(a)
        solution_count += 1

print("solution count = ", solution_count)


