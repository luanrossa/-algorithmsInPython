"""
Breadth-First Search (BFS) Algorithm in Python
----------------------------------------------

🔎 What is BFS?
- BFS is a graph traversal algorithm.
- It starts from a source node and explores all its neighbors first,
  before moving to the next level of neighbors.
- It visits nodes in breadth-first order (layer by layer).

⚡ Key Ideas:
1. Uses a queue (FIFO) to process nodes.
2. Keeps a 'visited' set to avoid revisiting nodes.
3. Ensures level-order traversal, making it useful to find the shortest path in unweighted graphs.

🛠️ Procedure:
1. Start with the source node.
2. Mark it visited and enqueue it.
3. While the queue is not empty:
   - Dequeue a node.
   - Visit it (record it).
   - Enqueue all its unvisited neighbors.

📊 Complexity:
- Time: O(V + E), where V = vertices, E = edges.
- Space: O(V), for the visited set and queue.

🎯 Use Cases:
- Shortest path in unweighted graphs (e.g., mazes, networks).
- Crawling/searching in networks or web pages.
- Level-order traversal of trees.
- Finding connected components in graphs.
"""


from collections import deque

def bfs(graph, start):
    """
    Breadth-First Search (BFS) traversal of a graph.
    
    :param graph: dict -> adjacency list representation of the graph
    :param start: starting node for BFS
    :return: list of nodes in BFS order
    """

    visited = set()           # Keep track of visited nodes
    queue = deque([start])    # Queue for BFS
    order = []                # Order of traversal

    while queue:
        node = queue.popleft()   # Get first element in the queue

        if node not in visited:
            visited.add(node)    # Mark as visited
            order.append(node)   # Save the visitation order

            # Add all unvisited neighbors to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

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
result = bfs(graph, start_node)
print("BFS traversal starting from", start_node, ":", result)
