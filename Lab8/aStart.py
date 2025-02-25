import heapq

GOAL_STATE = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

MOVES = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def find_zero(state):
    for i, row in enumerate(state):
        if 0 in row:
            return i, row.index(0)

def generate_neighbors(state):
    x, y = find_zero(state)
    neighbors = []
    for dx, dy in MOVES:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

def h1_misplaced_tiles(state):
    return sum(state[i][j] != GOAL_STATE[i][j] and state[i][j] != 0 for i in range(3) for j in range(3))

def h2_manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                goal_x, goal_y = divmod(state[i][j] - 1, 3)
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance

def astar(initial_state, heuristic):
    explored_count = 0
    fringe = []
    heapq.heappush(fringe, (0, initial_state, []))
    visited = set()

    while fringe:
        f, state, path = heapq.heappop(fringe)
        explored_count += 1
        if state == GOAL_STATE:
            return path, explored_count

        visited.add(str(state))

        for neighbor in generate_neighbors(state):
            if str(neighbor) not in visited:
                g = len(path) + 1
                h = heuristic(neighbor)
                heapq.heappush(fringe, (g + h, neighbor, path + [neighbor]))

    return None, explored_count

initial_state = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]

path_h1, explored_h1 = astar(initial_state, h1_misplaced_tiles)
path_h2, explored_h2 = astar(initial_state, h2_manhattan_distance)

print(f"H1 (Misplaced tiles):\nNodes explored: {explored_h1}\nSolution depth: {len(path_h1)}")
print(f"H2 (Manhattan distance):\nNodes explored: {explored_h2}\nSolution depth: {len(path_h2)}")
