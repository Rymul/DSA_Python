from collections import deque

# Has Path

# DFS iterative

def has_path(graph, src, dst):
    stack = [ src ]
    while stack:
        current = stack.pop()
        if current == dst:
            return True
        for neighbor in graph[current]:
            stack.append(neighbor)
    return False


# DFS recursive

def recursive_has_path(graph, src, dst):
    if src == dst:
        return True
    for neighbor in graph[src]:
        if recursive_has_path(graph, neighbor, dst) is True:
            return True
    return False

# BFS

def bfs_has_path(graph, src, dst):
    queue = deque([src])
    while queue:
        current = queue.popleft()
        if current == dst:
            return True    
        for neighbor in graph[current]:
            queue.append(neighbor)
    return False

# Undirected Path

def undirected_path(edges, node_A, node_B):
    graph = build_graph(edges)
    return has_path_helper(graph, node_A, node_B, set())


def has_path_helper(graph, src, dst, visited):
    if src == dst:
        return True
    if src in visited:
        return False
    visited.add(src)
    for neighbor in graph[src]:
        if has_path_helper(graph, neighbor, dst, visited) is True:
            return True
    return False

def build_graph(edges):
    graph = {}
    for edge in edges:
        a, b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph


# Connected Components Count

def connected_components_count(graph):
    visited = set()
    count = 0
    for node in graph:
        if explore(graph, node, visited) is True:
            count += 1
    return count

def explore(graph, current, visited):
    if current in visited:
        return False
    visited.add(current)
    for neighbor in graph[current]:
        explore(graph, neighbor, visited)
    return True

# Largest Component

def largest_component(graph):
    visited = set()
    max_size = 0
    for node in graph:
        count = adventure(graph, node, visited)
        if count > max_size:
            max_size = count
    return max_size

def adventure(graph, current, visited):
    if current in visited:
        return 0
    visited.add(current)
    count = 1
    for neighbor in graph[current]:
        count += adventure(graph, neighbor, visited)
    return count


# Shortest Path

def shortest_path(edges, node_A, node_B):
    visited = set([ node_A ])
    graph = make_graph(edges)
    queue = deque([ (node_A, 0) ])

    while queue:
        current, distance = queue.popleft()  
        if current == node_B:
            return distance
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))
    return -1

def make_graph(edges):
    graph = {}
    for edge in edges:
        a, b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph

# Island Count

def island_count(grid):
    visited = set()
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if travel(grid, row, col, visited) is True:
                count += 1
    return count
def travel(grid, row, col, visited):
    row_inbounds = 0 <= row < len(grid)
    col_inbounds = 0 <= col < len(grid[0])
    if not row_inbounds or not col_inbounds:
        return False
    if grid[row][col] == "W":
        return False
    pos = (row, col)
    if pos in visited:
        return False
    visited.add(pos)

    travel(grid, row - 1, col, visited)
    travel(grid, row + 1, col, visited)
    travel(grid, row, col - 1, visited)
    travel(grid, row, col + 1, visited)
    return True

# Minimum Size Island

def minimum_island(grid):
    visited = set()
    smallest = float('inf')
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            size = island_size(grid, r, c, visited)
            if size > 0 and size < smallest:
                smallest = size
    return smallest

def island_size(grid, r, c, visited):
    r_inbounds = 0 <=r < len(grid)
    c_inbounds = 0 <=c < len(grid[0])
    if not r_inbounds or not c_inbounds:
        return 0
    if grid[r][c] == "W":
        return 0
    pos = (r, c)
    if pos in visited:
        return 0
    visited.add(pos)
    size = 1
    size += island_size(grid, r -1, c, visited)
    size += island_size(grid, r +1, c, visited)
    size += island_size(grid, r, c -1, visited)
    size += island_size(grid, r, c +1, visited)
    return size
