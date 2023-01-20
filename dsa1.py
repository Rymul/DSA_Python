"""DS&A 1"""
# 217. Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


def contains_duplicate( nums ) -> bool:
    count = {}
    for num in nums:
        if num not in count:
            count[num] = 0
        count[num] += 1
        if count[num] > 1:
            return True
        
    return False

print(contains_duplicate([1,2,3,1]))
print(contains_duplicate([1,2,3]))   

# better answer:

def contains_duplicate2(nums) -> bool:
    unique = set(nums)
    if len(unique) < len(nums):
        return True
    return False


print(contains_duplicate2([1,2,3,1]))
print(contains_duplicate2([1,2,3]))



# Max Value

def max_value(nums) -> int:
    maxi = float('-inf')
    for num in nums:
        if num > maxi:
            maxi = num
    return maxi
    
print(max_value([4, 7, 2, 8, 10, 9]))
print(max_value([10, 5, 40, 40.3]))
print(max_value([-5, -2, -1, -11]))




# Is Prime

from math import sqrt, floor
def is_prime(n) -> int:
    if n < 2:
        return False
    for i in range(2, floor(sqrt(n)) +1):
        if n % i == 0:
            return False
    return True

print(is_prime(2))
print(is_prime(3))
print(is_prime(4))
print(is_prime(5))



# Uncompress

def uncompress(s) -> str:
    i = 0
    j = 0
    res = []
    nums = '0123456789'
    while j < len(s):
        if s[j] in nums:
            j += 1
        else:
            num = int(s[i:j])
            res.append(num * s[j])
            j += 1
            i = j
    return ''.join(res)

print(uncompress("2c3a1t"))



# Compress

def compress(s) -> str:
    s += '!'
    i = 0
    j = 0
    res = []
  
    while j < len(s):
        if s[j] == s[i]:
            j += 1
        else:
            num = j-i
            if num == 1:
                res.append(s[i])
            else:
                res.append(str(num))
                res.append(s[i])
            i = j
      
      
    return ''.join(res)

print(compress('ccaaatsss'))


# Anagrams
# time complexity O(n+m) where n = len(s1) and m = len(s2)

from collections import Counter

def anagrams(s1, s2) -> bool:
    return Counter(s1) == Counter(s2)
  # return char_count(s1) == char_count(s2)
  
  
# def char_count(s):
#   count = {}
  
#   for char in s:
#     if char not in count:
#       count[char] = 0
#     count[char] += 1
#   return count

print(anagrams('restful', 'fluster'))
print(anagrams('cats', 'tocs'))


# Most Frequent Char

def most_frequent_char(s) -> str:
    count = Counter(s)
    freq_char = None
    for char in s:
        if freq_char is None or count[char] > count[freq_char]:
            freq_char = char
    return freq_char

print(most_frequent_char('bookeeper'))



# Pair Sum

def pair_sum(numbers, target_sum):
  previous = {}
  
  for index, num in enumerate(numbers):
    comp = target_sum - num
    if comp in previous:
      return (previous[comp], index)
    previous[num] = index
    
print(pair_sum([3, 2, 5, 4, 1], 8))


# Pair Product

def pair_product(numbers, target_product):
  previous_nums = {}
  
  for index, num in enumerate(numbers):
    compliment = target_product / num
    if compliment in previous_nums:
      return (previous_nums[compliment], index)
    previous_nums[num] = index

print(pair_product([3, 2, 5, 4, 1], 8))



# Intersection

# from collections import Counter

# def intersection(a, b):
#   res = []
#   counter_b = Counter(b)
  
#   for num in a:
#     if num in counter_b:
#       res.append(num)
#   return res


def intersection(a, b):
  # res = []
  # items_set = set()
  
  # for item in a:
  #   items_set.add(item)
  # for ele in b:
  #   if ele in items_set:
  #     res.append(ele)
  # return res
  
  items_set = set(a)
  return [ ele for ele in b if ele in items_set ]

print(intersection([4,2,1,6], [3,6,9,2,10]))



# Five Sort

def five_sort(nums):
  i = 0
  j = len(nums) -1
  
  while i <= j:
    if nums[j] == 5:
      j -= 1
    elif nums[i] == 5:
      nums[i], nums[j] = nums[j], nums[i]
      i += 1
    else:
      i += 1
  return nums

print(five_sort([12, 5, 1, 5, 12, 7]))


# Linked List Values

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def linked_list_values(head):
  # res = []
  # curr = head
  # while curr is not None:
  #   res.append(curr.val)
  #   curr = curr.next
  # return res
  res = []
  linked_list_helper(head, res)
  return res
  
def linked_list_helper(head, res):
  if head is None:
    return
  res.append(head.val)
  linked_list_helper(head.next, res)
  

#Sum Linked List
def sum_list(head):
  total_sum = 0
  cur = head
  
  while cur is not None:
    total_sum += cur.val
    cur = cur.next
  
  return total_sum


#Recursive Sum Linked List

def recursive_sum_list(head):
  if head is None:
    return 0
  return head.val + recursive_sum_list(head.next)


# Linked List Find

def linked_list_find(head, target):
  cur = head
  while cur is not None:
    if cur.val == target:
      return True
    cur = cur.next
  return False


# Recursive Linked List Find

def recursive_linked_list_find(head, target):
  if head is None:
    return False
  if head.val == target:
    return True
  return recursive_linked_list_find(head.next, target)


# Get Node Value

def get_node_value(head, index):
  count = 0
  current = head
  
  while current is not None:
    if count == index:
      return current.val
    current = current.next
    count += 1
  return None

# Recursive Get Node Value

def recursive_get_node_value(head, index):
  if head is None:
    return None
  if index == 0:
    return head.val
  return get_node_value(head.next, index-1)


# Reverse Linked List

def reverse_list(head):
  current = head
  previous = None
  next_node = head.next
  
  while current is not None:
    next_node = current.next
    current.next = previous
    previous = current
    current = next_node
  return previous


# Recursive Reverse Linked List

def recursive_reverse_list(head, previous = None):
  if head is None:
    return previous
  next_node = head.next
  head.next = previous
  
  return recursive_reverse_list(next_node, head)


# Zipper List

def zipper_lists(head_1, head_2):
  tail = head_1
  current_1 = head_1.next
  current_2 = head_2
  count = 0
  
  while current_1 is not None and current_2 is not None:
    if count % 2 == 0:
      tail.next = current_2
      current_2 = current_2.next
    else:
      tail.next = current_1
      current_1 = current_1.next
    tail = tail.next
    count += 1
    
  if current_1 is not None:
    tail.next = current_1
  if current_2 is not None:
    tail.next = current_2
    
  return head_1

# Recursive Zipper List

def recursive_zipper_list(head_1, head_2):
    if head_1 is None and head_2 is None:
      return None
    if head_1 is None:
      return head_2
    if head_2 is None:
      return head_1
    
    next_1 = head_1.next
    next_2 = head_2.next
    head_1.next = head_2
    
    head_2.next = zipper_lists(next_1, next_2)
    return head_1


# Merge Lists

def merge_lists(head_1, head_2):
  current_1 = head_1
  current_2 = head_2
  dummy_head = Node(None)
  tail = dummy_head
    
  while current_1 is not None and current_2 is not None:
    if current_1.val < current_2.val:
      tail.next = current_1
      current_1 = current_1.next
    else:
      tail.next = current_2
      current_2 = current_2.next
    tail = tail.next
    
  if current_1 is not None:
    tail.next = current_1
  if current_2 is not None:
    tail.next = current_2
  return dummy_head.next


# Recursive Merge Lists

def recursive_merge_lists(head_1, head_2):
  if head_1 is None and head_2 is None:
    return None
  if head_1 is None:
    return head_2
  if head_2 is None:
    return head_1
  
  if head_1.val < head_2.val:
    next_1 = head_1.next
    head_1.next = recursive_merge_lists(next_1, head_2)
    return head_1
  else:
    next_2 = head_2.next
    head_2.next = recursive_merge_lists(head_1, next_2)
    return head_2


# Unique Value List
def is_univalue_list(head):
  current = head
  while current is not None:
    if head.val != current.val:
      return False
    current = current.next
  return True