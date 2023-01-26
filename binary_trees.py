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