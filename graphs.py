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

graph1 = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

print(has_path(graph1, 'f', 'k')) # True
print(recursive_has_path(graph1, 'f', 'k')) # True
print(bfs_has_path(graph1, 'f', 'k')) # True

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


edges1 = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

print(undirected_path(edges1, 'j', 'm')) # -> True

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

print(connected_components_count({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
})) # -> 2


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

print(largest_component({
  1: [2],
  2: [1,8],
  6: [7],
  9: [8],
  7: [6, 8],
  8: [9, 7, 2]
})) # -> 6

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

edges1 = [
  ['a', 'c'],
  ['a', 'b'],
  ['c', 'b'],
  ['c', 'd'],
  ['b', 'd'],
  ['e', 'd'],
  ['g', 'f']
]

print(shortest_path(edges1, 'a', 'e')) # -> 3


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

islands1 = [
  ['L', 'W', 'W', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['W', 'L', 'W', 'L', 'W'],
  ['W', 'W', 'W', 'W', 'W'],
  ['W', 'W', 'L', 'L', 'L'],
]

print(island_count(islands1)) # -> 4

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

islands2 = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

print(minimum_island(islands2)) # -> 2

# Closest Carrot

def closest_carrot(grid, starting_row, starting_col):
    visited = set([(starting_row, starting_col)])
    queue = deque([ (starting_row, starting_col, 0) ])
    while queue:
        row, col, distance = queue.popleft()
        if grid[row][col] == 'C':
            return distance
        deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for delta in deltas:
            delta_row, delta_col = delta
            neighbor_row = row + delta_row
            neighbor_col = col + delta_col
            row_inbounds = 0 <= neighbor_row < len(grid)
            col_inbounds = 0 <= neighbor_col < len(grid[0])
            pos = (neighbor_row, neighbor_col)
            if row_inbounds and col_inbounds and grid[neighbor_row][neighbor_col] != 'X' and pos not in visited:
                queue.append((neighbor_row, neighbor_col, distance +1))
                visited.add(pos)
    return -1


farm = [
  ['O', 'O', 'X', 'X', 'X'],
  ['O', 'X', 'X', 'X', 'C'],
  ['O', 'X', 'O', 'X', 'X'],
  ['O', 'O', 'O', 'O', 'O'],
  ['O', 'X', 'X', 'X', 'X'],
  ['O', 'O', 'O', 'O', 'O'],
  ['O', 'O', 'C', 'O', 'O'],
  ['O', 'O', 'O', 'O', 'O'],
]

print(closest_carrot(farm, 3, 4)) # -> 9


# Longest Path

def longest_path(graph):
    distance = {}
    for node in graph:
        if len(graph[node]) == 0:
            distance[node] = 0
    for node in graph:
        traverse_distance(graph, node, distance)
    return max(distance.values())


def traverse_distance(graph, node, distance):
    if node in distance:
        return distance[node]
    max_length = 0
    for neighbor in graph[node]:
        attempt = traverse_distance(graph, neighbor, distance)
        if attempt > max_length:
            max_length = attempt
    distance[node] = 1 + max_length
    return distance[node]

path_graph = {
  'a': ['c', 'b'],
  'b': ['c'],
  'c': [],
  'q': ['r'],
  'r': ['s', 'u', 't'],
  's': ['t'],
  't': ['u'],
  'u': []
}

print(longest_path(path_graph)) # -> 4

# Semesters Required

def semesters_required(num_courses, prereqs):
    graph = create_graph(num_courses, prereqs)
    distance = {}
    for course in graph:
        if len(graph[course]) == 0:
            distance[course] = 1
    for course in graph:
        traverse_distance(graph, course, distance)
    return max(distance.values())

def travel_distance(graph, node, distance):
    if node in distance:
        return distance[node]
    max_distance = 0
    for neighbor in graph[node]:
        neighbor_distance = travel_distance(graph, neighbor, distance)
        if neighbor_distance > max_distance:
            max_distance = neighbor_distance
    distance[node] = 1 + max_distance
    return distance[node]

def create_graph(num_courses, prereqs):
    graph = {}
    for course in range(num_courses):
        graph[course] = []
    for prereq in prereqs:
        a, b = prereq
        graph[a].append(b)
    return graph

n_courses = 6
prerequisits = [
  (1, 2),
  (2, 4),
  (3, 5),
  (0, 5),
]
print(semesters_required(n_courses, prerequisits)) # -> 3

# Best Bridge

def best_bridge(grid):
    main_island = None
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            potenial_island = find_an_island(grid, row, col, set())
            if len(potenial_island) > 0:
                main_island = potenial_island
                break
    visited = set(main_island)
    queue = deque([])
    for pos in main_island:
        row, col = pos
        queue.append((row, col, 0))
    while queue:
        row, col, distance = queue.popleft()
        if grid[row][col] == 'L' and (row,col) not in main_island:
            return distance -1
        deltas = [(-1,0),(1,0),(0,-1),(0,1)]
        for delta in deltas:
            delta_row, delta_col = delta
            neighbor_row = row + delta_row
            neighbor_col = col + delta_col
            neighbor_pos = (neighbor_row, neighbor_col)
            if is_inbouds(grid, neighbor_row, neighbor_col) and neighbor_pos not in visited:
                visited.add(neighbor_pos)
                queue.append((neighbor_row, neighbor_col, distance + 1))

def is_inbouds(grid, row, col):
    row_inbouds = 0 <= row < len(grid)
    col_inbouds = 0 <= col < len(grid[0])
    return row_inbouds and col_inbouds

def find_an_island(grid, row, col, visited):
    if not is_inbouds(grid, row, col) or grid[row][col] == "W":
        return visited
    pos = (row, col)
    if pos in visited:
        return visited
    visited.add(pos)

    find_an_island(grid, row -1, col, visited)
    find_an_island(grid, row +1, col, visited)
    find_an_island(grid, row, col -1, visited)
    find_an_island(grid, row, col +1, visited)
    return visited

construction_zone = [
  ["W", "W", "W", "L", "L"],
  ["L", "L", "W", "W", "L"],
  ["L", "L", "L", "W", "L"],
  ["W", "L", "W", "W", "W"],
  ["W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W"],
]
print(best_bridge(construction_zone))

# Has Cycle

def has_cycle(graph):
    visiting = set()
    visited = set()
    for node in graph:
        if cycle_detect(graph, node, visiting, visited):
            return True
    return False

def cycle_detect(graph, node, visiting, visited):
    if node in visited:
        return False
    if node in visiting:
        return True
    visiting.add(node)
    for neighbor in graph[node]:
        if cycle_detect(graph, neighbor, visiting, visited):
            return True
    visiting.remove(node)
    visited.add(node)
    return False

print(has_cycle({
  "a": ["b", "c"],
  "b": [],
  "c": [],
  "e": ["f"],
  "f": ["e"],
})) # -> True

print(has_cycle({
  "a": ["b", "c"],
  "b": ["c"],
  "c": ["d"],
  "d": [],
})) # -> False