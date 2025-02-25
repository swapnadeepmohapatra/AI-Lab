# Swapnadeep Mohapatra - 22053820

# Search for Treasure using the Best-First Search
# Problem
# Statement: The treasure is hidden in a grid, and each cell has a
# heuristic value representing its "closeness" to the treasure. Implement
# Best-First Search to locate the treasure.
#
# Tasks:
# *Use Euclidean Distance as a heuristic.
# *Implement the algorithm to always move to the most promising cell first (minimum heuristic value).

from queue import PriorityQueue

r = 7 # No. of edges

graph = [[] for i in range(r)]

priorityQueue = PriorityQueue()

explored = []

def addEdge(x, y, cost=0):
    graph[x].append((y, cost))
    graph[y].append((y, cost))


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


addEdge(0, 1, 3)
addEdge(0, 2, 2)
addEdge(1, 3, 5)
addEdge(1, 4, 1)
addEdge(2, 5, 6)
addEdge(2, 6, 0)

bfs(0, 6)
