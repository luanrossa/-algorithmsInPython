"""
A* (A-Star) Pathfinding Algorithm

Description:
    Finds the shortest path from a start node to a goal node in a graph or grid.
How it works:
    - Maintains an open set of nodes to explore and a closed set of visited nodes.
    - For each node, calculates:
        * g(n): cost from start to the current node
        * h(n): heuristic estimate to the goal (e.g., Manhattan distance)
        * f(n) = g(n) + h(n): total estimated cost
    - Repeatedly selects the node with the lowest f(n) from the open set, expands it,
      updates neighbors, and moves the node to the closed set.
    - Stops when the goal node is reached or no path exists.
Notes:
    - The heuristic h(n) must not overestimate to guarantee the shortest path.
    - Works efficiently for grids, maps, and general graphs.
"""


# The name of this arciive was 'A*.py' but the '*' character is not allowed in file names on some systems.
# So I renamed it to 'A-Star.py'.
import heapq

# -------------------------------
# Node structure (each position in the grid)
# -------------------------------
class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent      # Parent node (to reconstruct the path later)
        self.position = position  # Position in the grid (row, column)

        self.g = 0  # Cost from the start node to this node
        self.h = 0  # Heuristic estimated cost from this node to the goal
        self.f = 0  # Total cost = g + h

    def __eq__(self, other):
        return self.position == other.position

    # Required for the priority queue (heapq)
    def __lt__(self, other):
        return self.f < other.f


# -------------------------------
# Heuristic function (Manhattan distance)
# -------------------------------
def heuristic(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])


# -------------------------------
# A* Algorithm
# -------------------------------
def astar(maze, start, end):
    """
    maze  : 2D list where 0 = free space and 1 = obstacle
    start : tuple (row, column) for the start position
    end   : tuple (row, column) for the goal position
    """
    # Start and goal nodes
    start_node = Node(None, start)
    end_node = Node(None, end)

    # Open and closed lists
    open_list = []    # nodes to be explored
    closed_list = []  # nodes already explored

    # Add the start node to the open list
    heapq.heappush(open_list, start_node)

    # Loop until the solution is found or no nodes are left
    while open_list:
        # Get the node with the lowest f value
        current_node = heapq.heappop(open_list)
        closed_list.append(current_node)

        # Check if we reached the goal
        if current_node == end_node:
            path = []
            while current_node is not None:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Return reversed path (from start to goal)

        # Generate neighbors (left, right, up, down)
        neighbors = [
            (0, -1),  # left
            (0, 1),   # right
            (-1, 0),  # up
            (1, 0)    # down
        ]

        for move in neighbors:
            # Calculate neighbor position
            node_position = (current_node.position[0] + move[0],
                             current_node.position[1] + move[1])

            # Check if it's inside the grid boundaries
            if node_position[0] < 0 or node_position[0] >= len(maze) \
               or node_position[1] < 0 or node_position[1] >= len(maze[0]):
                continue

            # Check if it's an obstacle
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create a new neighbor node
            neighbor = Node(current_node, node_position)

            # If already explored, skip
            if neighbor in closed_list:
                continue

            # Calculate costs
            neighbor.g = current_node.g + 1
            neighbor.h = heuristic(neighbor.position, end_node.position)
            neighbor.f = neighbor.g + neighbor.h

            # If it's already in the open list with a lower g, skip
            if any(open_node for open_node in open_list if neighbor == open_node and neighbor.g > open_node.g):
                continue

            # Add to the open list
            heapq.heappush(open_list, neighbor)

    return None  # No path found


# -------------------------------
# Example usage
# -------------------------------
if __name__ == "__main__":
    # Example grid (0 = free, 1 = obstacle)
    maze = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0]
    ]

    start = (0, 0)  # starting point (row 0, column 0)
    end = (4, 4)    # goal point (row 4, column 4)

    path = astar(maze, start, end)
    print("Path found:", path)


