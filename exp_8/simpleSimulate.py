import random
from collections import defaultdict, deque

# Define a simple network graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
}

SOURCE = 'A'
DESTINATION = 'E'
TTL = 5  # Time to live for packets
BEST_PATHS = {
    'A': ['B'],
    'B': ['D'],
    'C': ['D'],
    'D': ['E']
}


def flood_all(graph, source, destination, ttl):
    return simulate(graph, source, destination, ttl, flood_mode='all')


def flood_except_input(graph, source, destination, ttl):
    return simulate(graph, source, destination, ttl, flood_mode='no_input')


def flood_best_k(graph, source, destination, ttl, k=2):
    return simulate(graph, source, destination, ttl, flood_mode='best_k', k=k)


def deterministic_routing(graph, source, destination, ttl):
    return simulate(graph, source, destination, ttl, flood_mode='best_k', k=1)


def simulate(graph, source, destination, ttl, flood_mode='all', k=2):
    queue = deque()
    # (current_node, previous_node, delay, ttl)
    queue.append((source, None, 0, ttl))
    reached_time = None
    transmissions = 0

    visited = set()

    while queue:
        current, previous, delay, ttl_left = queue.popleft()
        transmissions += 1

        if current == destination:
            if reached_time is None or delay < reached_time:
                reached_time = delay
            continue

        if ttl_left <= 0:
            continue

        # Decide neighbors to flood based on the mode
        if flood_mode == 'all':
            neighbors = graph[current]
        elif flood_mode == 'no_input':
            neighbors = [n for n in graph[current] if n != previous]
        elif flood_mode == 'best_k':
            neighbors = BEST_PATHS.get(current, graph[current])[:k]
        else:
            raise ValueError("Unknown flood mode")

        for neighbor in neighbors:
            if (neighbor, ttl_left - 1) not in visited:
                visited.add((neighbor, ttl_left - 1))
                queue.append((neighbor, current, delay + 1, ttl_left - 1))

    return reached_time, transmissions


# Run all simulations
ttl = TTL
print("Flood All:", flood_all(graph, SOURCE, DESTINATION, ttl))
print("Flood Except Input Line:", flood_except_input(
    graph, SOURCE, DESTINATION, ttl))
print("Flood Best k=2:", flood_best_k(graph, SOURCE, DESTINATION, ttl, k=2))
print("Deterministic (k=1):", deterministic_routing(
    graph, SOURCE, DESTINATION, ttl))
