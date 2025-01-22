# Maze Problem Solver using DFS

global counter
counter = 0

def is_safe(mat, visited, x, y):
    if x >= 0 and x < len(mat[0]) and y >= 0 and y < len(mat) and mat[x][y] == 1 and visited[x][y] == 0:
        return True
    return False


def solve_maze(mat, visited, x, y, dest_x, dest_y):
    global counter
    counter+=1

    if x == dest_x and y == dest_y:
        return True
    if is_safe(mat, visited, x, y):
        visited[x][y] = 1
        if solve_maze(mat, visited, x + 1, y, dest_x, dest_y):  # Right
            return True
        if solve_maze(mat, visited, x, y + 1, dest_x, dest_y):  # Down
            return True
        if solve_maze(mat, visited, x - 1, y, dest_x, dest_y):  # Left
            return True
        if solve_maze(mat, visited, x, y - 1, dest_x, dest_y):  # Up
            return True
        visited[x][y] = 0
        return False

    return False

mat = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1]
]

visited = [[0 for i in range(len(mat))] for j in range(len(mat[0]))]

src_row = 0
src_col = 0

dest_row = 2
dest_col = 2

if solve_maze(mat, visited, src_row, src_col, dest_row, dest_col):
    print("Path exists")
else:
    print("No path exists")

print("Comparisions", counter)

