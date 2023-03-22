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
