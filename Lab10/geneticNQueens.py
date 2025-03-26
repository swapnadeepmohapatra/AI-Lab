import random

N = 8
POP_SIZE = 200
MUTATION_RATE = 0.2
GENERATIONS = 1000

def fitness(board):
    non_attacking = 0
    for i in range(N):
        for j in range(i + 1, N):
            if board[i] != board[j] and abs(board[i] - board[j]) != (j - i):
                non_attacking += 1
    return non_attacking


def generate_board():
    return [random.randint(0, N - 1) for _ in range(N)]


def crossover(parent1, parent2):
    point = random.randint(1, N - 2)
    return parent1[:point] + parent2[point:]


def mutate(board):
    if random.random() < MUTATION_RATE:
        board[random.randint(0, N - 1)] = random.randint(0, N - 1)


def select(population):
    population.sort(key=lambda x: fitness(x), reverse=True)
    return population[:2]


def genetic_algorithm():
    population = [generate_board() for _ in range(POP_SIZE)]

    for generation in range(GENERATIONS):
        population.sort(key=lambda x: fitness(x), reverse=True)
        if fitness(population[0]) == 28:
            print(f"Solution found in {generation} generations.")
            return population[0]

        new_population = []
        for _ in range(POP_SIZE // 2):
            parent1, parent2 = select(population)
            child1, child2 = crossover(parent1, parent2), crossover(parent2, parent1)
            mutate(child1)
            mutate(child2)
            new_population.extend([child1, child2])

        population = new_population

    return None



solution = genetic_algorithm()
if solution:
    print("Solution:", solution)
else:
    print("No solution found within the given generations.")
