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
