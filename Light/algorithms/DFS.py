"""
Depth-First Search (DFS) Algorithm in Python
--------------------------------------------

🔎 What is DFS?
- DFS is a graph traversal algorithm.
- It starts from a source node and explores as far as possible
  along each branch before backtracking.
- It visits nodes in depth-first order.

⚡ Key Ideas:
1. DFS can be implemented using recursion (system call stack)
   or explicitly with a stack data structure.
2. Unlike BFS, DFS may not find the shortest path,
   but it is memory-efficient for large branching graphs.

🛠️ Procedure:
1. Start with the source node.
2. Mark it visited and process it.
3. Recursively (or via stack) visit each unvisited neighbor.
4. Backtrack when no unvisited neighbors remain.

📊 Complexity:
- Time: O(V + E), where V = vertices, E = edges.
- Space:
  - O(V) for recursion stack in worst case (deep graph).
  - More memory-efficient than BFS in wide graphs.

🎯 Use Cases:
- Pathfinding (when path length is not important).
- Detecting cycles in graphs.
- Topological sorting.
- Solving puzzles/mazes (backtracking problems).
"""

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
