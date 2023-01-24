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