def dfs(graph, start, visited=None):
    """
    Depth-First Search (DFS) traversal of a graph (recursive).
    
    :param graph: dict -> adjacency list representation of the graph
    :param start: starting node for DFS
    :param visited: set to keep track of visited nodes
    :return: list of nodes in DFS order
    """
    if visited is None:
        visited = set()

    visited.add(start)
    order = [start]

    for neighbor in graph[start]:
        if neighbor not in visited:
            order.extend(dfs(graph, neighbor, visited))

    return order


# ================== EXAMPLE ==================

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'
result = dfs(graph, start_node)
print("DFS traversal starting from", start_node, ":", result)