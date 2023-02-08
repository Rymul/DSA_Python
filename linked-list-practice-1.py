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

def recursive_sum_list(head):
    if head is None:
        return 0
    return head.val + recursive_sum_list(head.next)


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
print(recursive_sum_list(a))


def linked_list_find(head, target_val):
    current = head

    while current is not None:
        if current.val == target_val:
            return True
        current = current.next
    return False

print(linked_list_find(a, 7))
print(linked_list_find(a, 10))


def recursive_linked_list_find(head, target):
    if head is None:
        return False
    if head.val == target:
        return True
    return recursive_linked_list_find(head.next, target)

print(recursive_linked_list_find(a, 7))
print(recursive_linked_list_find(a, 10))


def get_node_value(head, index):
    current = head
    count = 0
    while current is not None:
        if count == index:
            return current.val
        count += 1
        current = current.next
    return None

print(get_node_value(a, 4))
print(get_node_value(a, 8))

def recursive_get_node_value(head, index):
    if head is None:
        return None
    if index == 0:
        return head.val
    return recursive_get_node_value(head.next, index -1)

print(recursive_get_node_value(a, 4))
print(recursive_get_node_value(a, 8))


def reverse_list(head):
    current = head
    prev = None
    while current is not None:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    return linked_list_values(prev)

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d
print(linked_list_values(a))
print(reverse_list(a))
