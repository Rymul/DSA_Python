class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def linked_list_values(head):
    res = []
    current = head
    while current is not None:
        res.append(current.val)
        current = current.next
    return res

def recursive_linked_list_values(head):
    res = []
    _recursive_linked_list_values(head, res)
    return res

def _recursive_linked_list_values(head, res):
    if head is None:
        return []
    res.append(head.val)
    _recursive_linked_list_values(head.next, res)

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

print(linked_list_values(a))
print(recursive_linked_list_values(a))


def sum_list(head):
    list_sum = 0
    current = head
    while current is not None:
        list_sum += current.val
        current = current.next
    return list_sum

a = Node(2)
b = Node(8)
c = Node(3)
d = Node(-1)
e = Node(7)

a.next = b
b.next = c
c.next = d
d.next = e

print(sum_list(a))
