class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# DFS values

def depth_first_values(root):
    if root is None:
        return []
    stack = [root]
    res = []
    while stack:
        current = stack.pop()
        res.append(current.val)
        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)
    return res

# Recursive DFS values

def recursive_depth_first_values(root):
    if root is None:
        return []
    left_vals = depth_first_values(root.left)
    right_vals = depth_first_values(root.right)
    # return [root.val, *left_vals, *right_vals]
    return [root.val] + left_vals + right_vals


# BFS Binary Tree

from collections import deque

def breadth_first_values(root):
    if root is None:
        return []
    queue = deque([ root ])
    res = []
    while queue:
        current = queue.popleft()
        res.append(current.val)
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)
    return res


# Sum Tree

# using DFS

def tree_sum(root):
    if root is None:
        return 0
    return root.val + tree_sum(root.left) + tree_sum(root.right)

# using BFS

def bfs_tree_sum(root):
    if root is None:
        return 0
    total_sum = 0
    queue = deque( [root] )
    while queue:
        current = queue.popleft()
        total_sum += current.val

        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)
    return total_sum

# Tree Includes

# using BFS

def tree_includes(root, target):
    if root is None:
        return False
    queue = deque( [root] )
    while queue:
        current = queue.popleft()
        if current.val == target:
            return True
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)
    return False

# using DFS

def dfs_tree_includes(root, target):
    if root is None:
        return False
    if root.val == target:
        return True
    return dfs_tree_includes(root.left, target) or dfs_tree_includes(root.right, target)

# Tree Min Value

# using BFS

def tree_min_value(root):
    queue = deque( [root] )
    min_val = float('inf')
    while queue:
        current = queue.popleft()
        if current.val < min_val:
            min_val = current.val
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)
    return min_val

# using DFS interative

def interative_dfs_tree_min_value(root):
    stack = [ root ]
    min_val = float('inf')
    while stack:
        current = stack.pop()
        if current.val < min_val:
            min_val = current.val
        if current.left is not None:
            stack.append(current.left)
        if current.right is not None:
            stack.append(current.right)
    return min_val

# using recursive DFS

def recursive_dfs_tree_min_value(root):
    if root is None:
        return float('inf')
    min_left = recursive_dfs_tree_min_value(root.left)
    min_right = recursive_dfs_tree_min_value(root.right)
    return min(root.val, min_left, min_right)

# Max Root to Leaf Sum

def max_path_sum(root):
    if root is None:
        return float('-inf')
    if root.left is None and root.right is None:
        return root.val
    max_left = max_path_sum(root.left)
    max_right = max_path_sum(root.right)
    return root.val + max(max_left, max_right)

# Path Finder

def path_finder(root, target):
    res = _path_finder(root, target)
    if res is None:
        return None
    return res[::-1]

def _path_finder(root, target):
    if root is None:
        return None
    if root.val == target:
        return [root.val]
    left_path = _path_finder(root.left, target)
    if left_path is not None:
        left_path.append(root.val)
        return left_path
    right_path = _path_finder(root.right, target)
    if right_path is not None:
        right_path.append(root.val)
        return right_path
    return None

# Tree Value Count 

# recursive 
def recursive_tree_value_count(root, target):
    if root is None:
        return 0
    match = 1 if root.val == target else 0
    return match + recursive_tree_value_count(root.left, target) + recursive_tree_value_count(root.right, target)

# using BFS
def tree_value_count(root, target):
    if root is None:
        return 0
    queue = deque( [root] )
    count = 0
    while queue:
        current = queue.popleft()
        if current.val == target:
            count += 1
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)
    return count

# Tree Height

def how_high(node):
    if node is None:
        return -1
    left_height = how_high(node.left)
    right_height = how_high(node.right)
    return 1 + max(left_height, right_height)


# Bottom Right Value

def bottom_right_value(root):
    queue = deque( [root] )
    current = None
    while queue:
        current = queue.popleft()
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)
    return current.val

# All Tree Paths

def all_tree_paths(root):
    if root is None:
        return []
    if root.left is None and root.right is None:
        return [[root.val]]
    paths = []
    left_paths = all_tree_paths(root.left)
    for sub_path in left_paths:
        paths.append([root.val, *sub_path])
    right_paths = all_tree_paths(root.right)
    for sub_path in right_paths:
        paths.append([root.val, *sub_path])
    return paths

# Tree Levels

# DFS iterative

def dfs_tree_levels(root):
    if root is None:
        return []
    levels = []
    stack = [ (root, 0) ]
    while stack:
        node, level_num = stack.pop()
        if len(levels) == level_num:
            levels.append([node.val])
        else:
            levels[level_num].append(node.val)

        if node.right is not None:
            stack.append((node.right, level_num + 1))
        if node.left is not None:
            stack.append((node.left, level_num + 1))
    return levels

# BFS iterative

def bfs_tree_levels(root):
    if root is None:
        return []
    levels = []
    queue = deque([ (root, 0) ])
    while queue:
        node, level_num = queue.popleft()
        if len(levels) == level_num:
            levels.append([node.val])
        else:
            levels[level_num].append(node.val)
        if node.left is not None:
            queue.append((node.left, level_num + 1))
        if node.right is not None:
            queue.append((node.right, level_num + 1))
    return levels

# Recursive DFS

def tree_levels(root):
    levels = []
    fill_levels(root, levels, 0)
    return levels

def fill_levels(root, levels, level_num):
    if root is None:
        return
    if len(levels) == level_num:
        levels.append( [root.val] )
    else:
        levels[level_num].append(root.val)
  
    fill_levels(root.left, levels, level_num + 1)
    fill_levels(root.right, levels, level_num + 1)


# Level Averages

from statistics import mean

def level_averages(root):
    levels = []
    make_levels(root, levels, 0)
    avg = []
    for sub_list in levels:
        avg.append(mean(sub_list))
    return avg

def make_levels(root, levels, level_num):
    if root is None:
        return
    if len(levels) == level_num:
        levels.append([root.val])
    else:
        levels[level_num].append(root.val)
    make_levels(root.left, levels, level_num + 1)
    make_levels(root.right, levels, level_num + 1)


# Leaf List

# Iterative DFS

def leaf_list(root):
    if root is None:
        return []
    leaves = []
    stack = [root]
    while stack:
        current = stack.pop()
        if current.left is None and current.right is None:
            leaves.append(current.val)
        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)
    return leaves

# Recursive DFS

def recursive_leaf_list(root):
    leaves = []
    _leaf_list(root, leaves)
    return leaves

def _leaf_list(root, leaves):
    if root is None:
        return []
    if root.left is None and root.right is None:
        leaves.append(root.val)

    _leaf_list(root.left, leaves) 
    _leaf_list(root.right, leaves)
