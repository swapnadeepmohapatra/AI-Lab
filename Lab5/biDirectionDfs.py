# Assignment 3: Search for Treasure using the Best-First Search
# Objective: Use Best-First Search to find a treasure in a grid.
# Problem Statement: The treasure is hidden in a grid, and each cell has a heuristic
# value representing its "closeness" to the treasure. Implement Best-First Search to
# locate the treasure.
# Tasks:
# ⚫ Use Manhattan distance as a heuristic.
# ⚫ Implement the algorithm to always move to the most promising cell first
# (minimum heuristic value).
# ⚫ Analyze how heuristic choice affects performance.

grid = [
    [0,0,0,1],
    [1,0,0,1],
    [1,0,1,1],
    [1,0,0,0],
]

priorityQueue = []

# Using manhattan distance
def getHeuristic(v1, v2):
    return abs(v1[0] - v2[0]) + abs(v1[1] - v2[1])
