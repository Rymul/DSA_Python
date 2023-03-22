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
