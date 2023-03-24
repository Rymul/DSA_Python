from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def depth_first_values(root):
    if root is None:
        return []
    left = depth_first_values(root.left)
    right = depth_first_values(root.right)
    return [root.val] + left + right

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')        
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

print(depth_first_values(a))
#   -> ['a', 'b', 'd', 'e', 'c', 'f']

def breadth_first_values(root):
    if root is None:
        return []
    queue = deque([root])
    res = []
    while queue:
        current = queue.popleft()
        res.append(current.val)
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)
    return res

print(breadth_first_values(a))

def tree_sum(root):
    if root is None:
        return 0
    queue = deque([root])
    total_sum = 0
    while queue:
        current = queue.popleft()
        total_sum += current.val
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)
    return total_sum

def recursive_tree_sum(root):
    if root is None:
        return 0
    return root.val + recursive_tree_sum(root.left) + recursive_tree_sum(root.right)

a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1

print(tree_sum(a)) # -> 21
print(recursive_tree_sum(a))

def tree_includes(root, target):
    if root.val == target:
        return True
    queue = deque([root])
    while queue:
        current = queue.popleft()
        if current.val == target:
            return True
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)
    return False

def recursive_tree_includes(root, target):
    if root is None:
        return False
    if root.val == target:
        return True
    return recursive_tree_includes(root.left, target) or recursive_tree_includes(root.right, target)

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

print(tree_includes(a, "e")) # -> True
print(tree_includes(a, "z")) # -> False
print(recursive_tree_includes(a, "e")) # -> True
print(recursive_tree_includes(a, "z")) # -> False


def tree_min_value(root):
    queue = deque([root])
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

def recursive_tree_min_value(root):
    if root is None:
        return float('inf')
    min_left = recursive_tree_min_value(root.left)
    min_right = recursive_tree_min_value(root.right)
    return min(root.val, min_left, min_right)

a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1

print(tree_min_value(a)) # -> -2
print(recursive_tree_min_value(a))


def max_path_sum(root):
    if root is None:
        return float('-inf')
    if root.left is None and root.right is None:
        return root.val
    max_left = max_path_sum(root.left)
    max_right = max_path_sum(root.right)
    return root.val + max(max_left, max_right)

a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1

print(max_path_sum(a)) # -> 18

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

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

print(path_finder(a, 'e')) # -> [ 'a', 'b', 'e' ]


def tree_value_count(root, target):
    queue = deque([root])
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

def recursive_tree_value_count(root, target):
    if root is None:
        return 0
    match = 1 if root.val == target else 0
    return match + recursive_tree_value_count(root.left, target) + recursive_tree_value_count(root.right, target)

a = Node(12)
b = Node(6)
c = Node(6)
d = Node(4)
e = Node(6)
f = Node(12)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      12
#    /   \
#   6     6
#  / \     \
# 4   6     12

print(tree_value_count(a,  6)) # -> 3
print(recursive_tree_value_count(a, 6))
