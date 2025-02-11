from queue import PriorityQueue

r = 7  # No. of nodes

graph = [[] for i in range(r)]

priorityQueue = PriorityQueue()

explored = []


def bfs(start, goal):
    priorityQueue.put((0, start))
    explored.append(start)
    while not priorityQueue.empty():
        v = priorityQueue.get()

        print(v[1], end=" ")

        if v[1] == goal:
            print("Goal reached")
            break

        for u, cost in graph[v[1]]:
            if u not in explored:
                explored.append(u)
                priorityQueue.put((cost, u))

def addEdge(x, y, cost):
    graph[x].append((y, cost))
    graph[y].append((x, cost))


addEdge(0, 1, 3)
addEdge(0, 2, 2)
addEdge(1, 3, 5)
addEdge(1, 4, 1)
addEdge(2, 5, 6)
addEdge(2, 6, 0)

bfs(0, 6)
