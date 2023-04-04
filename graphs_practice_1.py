from collections import deque

def has_path_1(graph, src, dst):
    queue = deque([src])
    while queue:
        current = queue.popleft()
        if current == dst:
            return True
        for neighbor in graph[current]:
            queue.append(neighbor)
    return False

def recursive_has_path_1(graph, src, dst):
    if src == dst:
        return True
    for neighbor in graph[src]:
        if recursive_has_path_1(graph, neighbor, dst) is True:
            return True
    return False

graph_1 = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}
graph_2 = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}


print(has_path_1(graph_1, 'f', 'k')) # True
print(has_path_1(graph_2, 'f', 'j')) # False
print(recursive_has_path_1(graph_1, 'f', 'k')) # True
print(recursive_has_path_1(graph_2, 'f', 'j')) # False



def undirected_path(edges, node_A, node_B):
    graph = build_graph(edges)
    return has_path(graph, node_A, node_B, set())

  
def has_path(graph, src, dst, visited):
    if src == dst:
        return True
    if src in visited:
        return False
    visited.add(src)
    for neighbor in graph[src]:
        if has_path(graph, neighbor, dst, visited) is True:
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

edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

print(undirected_path(edges, 'j', 'm')) # -> True


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

print(connected_components_count({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
})) # -> 2


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

print(largest_component({
  1: [2],
  2: [1,8],
  6: [7],
  9: [8],
  7: [6, 8],
  8: [9, 7, 2]
})) # -> 6