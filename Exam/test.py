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

n = 7

graph = [[] for i in range(n)]

priorityQueue = PriorityQueue()

explored = []

def addEdge(graph, x, y, cost=0):
    graph[x].append((y, cost))
    graph[y].append((y, cost))


def bfs(start, goal):
    priorityQueue.put((0, start))
    explored.append(start)
    while not priorityQueue.empty():
        v = priorityQueue.get()

        print(v[1], end=" -> ")

        if v[1] == goal:
            print("\b\b\b\b\nGoal reached")
            break

        for u, cost in graph[v[1]]:
            if u not in explored:
                explored.append(u)
                priorityQueue.put((cost, u))


addEdge(graph, 0, 0, 0)
addEdge(graph, 0, 1, 5)
addEdge(graph, 0, 2, 4)
addEdge(graph, 0, 3, 8)
addEdge(graph, 1, 4, 3)
addEdge(graph, 2, 5, 3)
addEdge(graph, 3, 6, 1)

bfs(0, 6)
