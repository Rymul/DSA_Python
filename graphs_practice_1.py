from collections import deque

def has_path(graph, src, dst):
    queue = deque([src])
    while queue:
        current = queue.popleft()
        if current == dst:
            return True
        for neighbor in graph[current]:
            queue.append(neighbor)
    return False

def recursive_has_path(graph, src, dst):
    if src == dst:
        return True
    for neighbor in graph[src]:
        if recursive_has_path(graph, neighbor, dst) is True:
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


print(has_path(graph_1, 'f', 'k')) # True
print(has_path(graph_2, 'f', 'j')) # False
print(recursive_has_path(graph_1, 'f', 'k')) # True
print(recursive_has_path(graph_2, 'f', 'j')) # False

