# maze = [
#     [1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1],
#     [1, 1, 1, 0, 1],
#     [1, 1, 0, 1, 1],
#     [1, 1, 1, 1, 1]
# ]

maze = [
    [1,1,0],
    [1,1,0],
    [1,1,1],
]

start = (1, 1)
end = (3, 3)
global counter
counter = 0


def bfs(start, end, maze):
    global counter
    queue = []
    r = len(maze)
    c = len(maze[0])

    visited = [[0 for i in range(c)] for j in range(r)]
    visited[start[0]][start[1]] = True
    queue.append((start[0], start[1], 0, f'({start[0]}, {start[1]}) '))
    while len(queue) != 0:
        p = queue.pop(0)
        counter+=1

        if maze[p[0]][p[1]] == 0:
            continue
        if p[0] == end[0] and p[1] == end[1]:
            return p[3]
        if p[0] + 1 < r and visited[p[0] + 1][p[1]] == False:
            queue.append((p[0] + 1, p[1], p[2] + 1, p[3] + f'({p[0] + 1}, {p[1]}) '))
            visited[p[0] + 1][p[1]] = True
        if p[0] - 1 >= 0 and visited[p[0] - 1][p[1]] == False:
            queue.append((p[0] - 1, p[1], p[2] + 1, p[3] + f'({p[0] - 1}, {p[1]}) '))
            visited[p[0] - 1][p[1]] = True
        if p[1] + 1 < c and visited[p[0]][p[1] + 1] == False:
            queue.append((p[0], p[1] + 1, p[2] + 1, p[3] + f'({p[0]}, {p[1] + 1}) '))
            visited[p[0]][p[1] + 1] = True
        if p[1] - 1 >= 0 and visited[p[0]][p[1] - 1] == False:
            queue.append((p[0], p[1] - 1, p[2] + 1, p[3] + f'({p[0]}, {p[1] - 1}) '))
            visited[p[0]][p[1] - 1] = True
    return -1


print(f'Shortest Path Using BFS: {bfs(start, end, maze)}')
print("Comparisons", counter)