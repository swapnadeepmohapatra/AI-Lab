import heapq


def uniform_cost_search(graph, start, goal):
    priority_queue = [(0, start)]
    visited = {start: (0, None)}

    while priority_queue:
        current_cost, current_node = heapq.heappop(priority_queue)

        if current_node == goal:
            return current_cost, reconstruct_path(visited, goal)

        for neighbor, cost in graph[current_node]:
            total_cost = current_cost + cost
            if neighbor not in visited or total_cost < visited[neighbor][0]:
                visited[neighbor] = (total_cost, current_node)
                heapq.heappush(priority_queue, (total_cost, neighbor))

    return None

def reconstruct_path(visited, goal):
    const_path = []
    current = goal
    while current is not None:
        const_path.append(current)
        current = visited[current][1]  # Get the parent node
    const_path.reverse()
    return const_path

graph = {
    'A': [('B', 1), ('C', 3), ('D', 5)],
    'B': [('E', 3)],
    'C': [('F', 5)],
    'D': [('G', 3)],
    'E': [],
    'F': [],
    'G': [('H', 1)],
    'H': [],
}

start_node = 'A'
goal_node = 'H'
result = uniform_cost_search(graph, start_node, goal_node)

if result:
    total_cost, path = result
    print(f"Least cost path from {start_node} to {goal_node}: {' -> '.join(path)} with total cost {total_cost}")

else:
    print(f"No path found from {start_node} to {goal_node}")