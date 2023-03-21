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


def recursive_reverse_list(head, prev = None):
    if head is None:
        return prev
    temp = head.next
    head.next = prev
    return recursive_reverse_list(temp, head)

print(recursive_reverse_list(a))

def zipper_lists(head_1, head_2):
    tail = head_1
    cur_1 = head_1.next
    cur_2 = head_2
    count = 0
    while cur_1 is not None and cur_2 is not None:
        if count % 2 == 0:
            tail.next = cur_2
            cur_2 = cur_2.next
        else:
            tail.next = cur_1
            cur_1 = cur_1.next
        tail = tail.next
        count += 1
    if cur_1 is not None:
        tail.next = cur_1
    if cur_2 is not None:
        tail.next = cur_2
    return linked_list_values(head_1)

a = Node("a")
b = Node("b")
c = Node("c")
a.next = b
b.next = c
# a -> b -> c

x = Node("x")
y = Node("y")
z = Node("z")
x.next = y
y.next = z
# x -> y -> z

print(zipper_lists(a, x))

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
# a -> b -> c -> d -> e -> f

x = Node("x")
y = Node("y")
z = Node("z")
x.next = y
y.next = z
# x -> y -> z

print(zipper_lists(a, x))
# a -> x -> b -> y -> c -> z -> d -> e -> f

def merge_lists(head_1, head_2):
    dummy_head = Node(None)
    tail = dummy_head
    cur_1 = head_1
    cur_2 = head_2

    while cur_1 is not None and cur_2 is not None:
        if cur_1.val <= cur_2.val:
            tail.next = cur_1
            cur_1 = cur_1.next
        else:
            tail.next = cur_2
            cur_2 = cur_2.next
        tail = tail.next

    if cur_1 is not None:
        tail.next = cur_1
    if cur_2 is not None:
        tail.next = cur_2
    return linked_list_values(dummy_head.next)

a = Node(5)
b = Node(7)
c = Node(10)
d = Node(12)
e = Node(20)
f = Node(28)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
# 5 -> 7 -> 10 -> 12 -> 20 -> 28

q = Node(6)
r = Node(8)
s = Node(9)
t = Node(25)
q.next = r
r.next = s
s.next = t
# 6 -> 8 -> 9 -> 25

print(merge_lists(a, q))
# 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 12 -> 20 -> 25 -> 28 

def is_univalue_list(head):
    current = head
    while current is not None:
        if current.val != head.val:
            return False
        current = current.next
    return True

def recursive_is_univalue_list(head, prev_val = None):
    if head is None:
        return True
    if prev_val is not None and prev_val != head.val:
        return False
    return recursive_is_univalue_list(head.next, head.val)

u = Node(2)
v = Node(2)
w = Node(2)
x = Node(2)
y = Node(2)

u.next = v
v.next = w
w.next = x
x.next = y

# 2 -> 2 -> 2 -> 2 -> 2

print(is_univalue_list(u)) # True
print(is_univalue_list(a)) # False
print(recursive_is_univalue_list(u)) # True
print(recursive_is_univalue_list(a)) # False


def longest_streak(head):
    current = head
    prev_val = None
    count = 0
    max_count = 0
    while current is not None:
        if current.val == prev_val:
            count += 1
        else:
            count = 1
        if count > max_count:
            max_count = count
        prev_val = current.val
        current = current.next
    return max_count

a = Node(3)
b = Node(3)
c = Node(3)
d = Node(3)
e = Node(9)
f = Node(9)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# 3 -> 3 -> 3 -> 3 -> 9 -> 9

print(longest_streak(a)) # 4


def removeNode(head, target):
    if head.val == target:
        return head.next
    current = head
    prev = None

    while current is not None:
        if current.val == target:
            prev.next = current.next
            break
        prev = current
        current = current.next
    return head

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

print(removeNode(a, "c"))


# 141. Linked List Cycle

def hasCycle(head):
    visited = set()
    current = head
    while current is not None:
        if current in visited:
            return True
        visited.add(current)
        current = current.next
    return False

print(hasCycle(a)) # False
f.next = a
print(hasCycle(a)) # True


# 278. First Bad Version
# function first bad version is given

# def firstBadVersion(n):
#     left = 1
#     right = n
#     while left < right:
#         mid = left + (right - left)//2
#         if isBadversion(mid):
#             right = mid
#         else:
#             left = mid + 1
#     return left


# 28. Find the Index of the First Occurrence in a String

def strStr(haystack, needle):
    return haystack.find(needle)

h = "sadbutsad" 
n = "sad"
print(strStr(h, n)) # 0


def insert_node(head, value, index):
    if index == 0:
        new_head = Node(value)
        new_head.next = head
        return new_head
    current = head
    count = 0

    while current is not None:
        if count == index -1:
            temp = current.next
            current.next = Node(value)
            current.next.next = temp
        current = current.next
        count += 1
    return head

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

print(insert_node(a, 'x', 2))
# a -> b -> x -> c -> d



def create_linked_list(list_values):
    dummy = Node(None)
    for i, ele in enumerate(list_values):
        if i == 0:
            dummy.next = Node(ele)
            current = dummy.next
        else:
            current.next = Node(ele)
            current = current.next
    return dummy.next

print(create_linked_list(["h", "e", "y"]))
print(create_linked_list([]))