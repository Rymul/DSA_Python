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
  