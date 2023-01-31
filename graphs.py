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