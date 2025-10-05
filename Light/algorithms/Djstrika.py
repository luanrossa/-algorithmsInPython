"""
Dijkstra's Algorithm
Author: Luan Rossa

Description:
    Implements Dijkstra's algorithm to find the shortest distance 
    from a starting node to all other nodes in a weighted graph.

How it works:
    - Maintains a dictionary of minimum known distances to each node.
    - Uses a priority queue (min-heap) to always explore the node 
      with the smallest current distance.
    - For each neighbor of the current node, calculates the tentative 
      distance and updates it if smaller than the previously known distance.
    - Continues until all nodes have been processed, guaranteeing 
      the shortest distance from the start node to every other node.

Notes:
    - Graph is represented as a dictionary where keys are nodes 
      and values are lists of tuples (neighbor, weight).
    - Returns a dictionary of minimum distances from the start node.
"""

import heapq  # Library for using a priority queue (always keeps the minimum cost at the top)

def dijkstra(graph, start):
    """
    Dijkstra's algorithm implementation to find
    the shortest distance from a start node to all other nodes in a graph.

    :param graph: dictionary where keys are nodes and values are lists of tuples (neighbor, weight)
    :param start: starting node
    :return: dictionary with minimum distances from the start node to each node
    """

    # Dictionary to store the minimum known distance to each node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  # Distance from start node to itself is 0

    # Priority queue to always pick the node with the smallest distance
    queue = [(0, start)]  # (distance, node)

    while queue:
        # Extract the node with the smallest accumulated distance so far
        current_distance, current_node = heapq.heappop(queue)

        # If we already found a better path, skip this one
        if current_distance > distances[current_node]:
            continue

        # Explore neighbors of the current node
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight  # accumulated cost

            # If a shorter path to the neighbor is found, update it
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # Add it to the queue to explore later
                heapq.heappush(queue, (distance, neighbor))

    return distances


# ================== EXAMPLE USAGE ==================

# Graph represented as adjacency list
# Each key is a node, and the value is a list of (neighbor, weight)
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

start = 'A'
result = dijkstra(graph, start)

print("Shortest distances from node", start)
for node, distance in result.items():
    print(f"{start} -> {node} = {distance}")
