from collections import Counter, deque

# 118. Pascal's Triangle

def pascalsTriangle(numRows) -> list:
    pascal=[[1]]
    for i in range(1, numRows):
        curr = [1]
        for j in range(1, i):
            curr.append(prev[j]+prev[j-1])
        curr.append(1)
        pascal.append(curr)
        prev=curr
    return pascal

print(pascalsTriangle(5))
print(pascalsTriangle(1))

# 119. Pascal's Triangle II

def pascalsTriangle2(rowIndex)-> list:
    prev=[1]
    for i in range(1,1+rowIndex):
        curr=[1]
        for j in range(1,i):
            curr.append(prev[j]+prev[j-1])
        curr.append(1)
        prev=curr
    return prev

print(pascalsTriangle2(3))
print(pascalsTriangle2(1))

# 121. Best Time to Buy and Sell Stock

def maxProfit(prices) -> int:
    if not prices:
        return 0
    max_return = 0
    min_buy = prices[0]
    for price in prices:
        max_return = max(price - min_buy, max_return)
        if price < min_buy:
            min_buy = price
    return max_return

print(maxProfit([7,1,5,3,6,4])) # 5


# 125. Valid Palindrome

def isPalindrome(s) -> bool:
    mod_str = (''.join(char for char in s if char.isalnum())).lower()
    return mod_str == mod_str[::-1]

print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("Race a car"))

# 136. Single Number

def singleNumber(nums) -> int:
    n = len(nums)
    num = nums[0]
    for i in range(1,n):
        num = num ^ nums[i] 
    return num

print(singleNumber([4,1,2,1,2]))

# 145. Binary Tree Postorder Traversal

def postorderTraversal(root) -> list:
    if root is None:
        return []
    res = []
    stack = [root]
    while stack:
        current = stack.pop()
        res.append(current.val)
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
    return res[::-1]

# 160. Intersection of Two Linked Lists

def getIntersectionNode(headA, headB):
    first = set()
    curr = headA
    while curr:
        first.add(curr)
        curr = curr.next
    curr = headB
    while curr:
        if curr in first:
            return curr
        curr = curr.next
    return None

# 168. Excel Sheet Column Title

def convertToTitle(columnNumber) -> str:
    res = ""
    while columnNumber > 0:
        res = chr(ord('A') + (columnNumber - 1) % 26) + res
        columnNumber = (columnNumber - 1) // 26
    return res

print(convertToTitle(2))
print(convertToTitle(728))

# 169. Majority Element

def majorityElement(nums) -> int:
    counter = Counter(nums)
    for n, c in counter.items():
        if c > (len(nums)/2):
            return n

print(majorityElement([2,2,1,1,1,2,2]))

# 387. First Unique Character in a String

def firstUniqChar(s) -> int:
    counter = Counter(s)
    for i, char in enumerate(s):
        if counter[s[i]] == 1:
            return i
    return -1

print(firstUniqChar("loveleetcode"))

# 557. Reverse Words in a String III

def reverseWords(s) -> str:
    arr = s.split(" ")
    arr = [i[::-1] for i in arr]
    return " ".join(arr)

print(reverseWords('Wow, this works very nice'))

# 559. Maximum Depth of N-ary Tree
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        depth = 1
        if root.children:
            depth += max(self.maxDepth(child) for child in root.children)
        return depth

# 561. Array Partition

def arrayPairSum(nums) -> int:
    nums.sort()
    res_sum = 0
    for i in range(0,len(nums),2):
        res_sum += nums[i]
    return res_sum

print(arrayPairSum([6,2,6,5,1,2])) #9

# 617. Merge Two Binary Trees

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def mergeTrees(root1, root2):
    if not root1:
        return root2
    elif not root2:
        return root1
    else:
        res = TreeNode(root1.val + root2.val)
        res.left = mergeTrees(root1.left, root2.left)
        res.right = mergeTrees(root1.right, root2.right)
    return res

# 628. Maximum Product of Three Numbers

def maximumProduct(nums) -> int:
    nums.sort()
    return max(nums[0]*nums[1]*nums[-1], nums[-1]*nums[-2]*nums[-3])

print(maximumProduct([1,2,3,4,5]))

# 637. Average of Levels in Binary Tree

def averageOfLevels(root):
    queue = deque([root])
    average_of_level = []
    while queue:
        size = len(queue)
        totalSum = 0
        for _ in range(size):
            node = queue.popleft()
            totalSum += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        average_of_level.append(totalSum/size)
    return average_of_level

# 507. Perfect Number

def checkPerfectNumber(num) -> bool:
    if num == 1:
        return False
    res = 1
    for i in range(2,int(num ** 0.5) + 1):
        if num % i == 0:
            res += i + num//i
    return res == num

print(checkPerfectNumber(28))
print(checkPerfectNumber(7))

# 509. Fibonacci Number

def fib(n) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(3))


# 520. Detect Capital
def detectCapitalUse(word) -> bool:
    return word in [word.lower(), word.upper(), word.capitalize()]

print(detectCapitalUse('USA'))
print(detectCapitalUse("FalSE"))

# 202. Happy Number

def isHappy(n) -> bool:
    visited = set()
    while n != 1:
        if n in visited: return False
        visited.add(n)
        n = sum([int(i) ** 2 for i in str(n)])
        if n == 1:
            return True

print(isHappy(19))
print(isHappy(2))

# 205. Isomorphic Strings

def isIsomorphic(s, t) -> bool:
    map1 = []
    map2 = []
    for i in s:
        map1.append(s.index(i))
    for i in t:
        map2.append(t.index(i))
    if map1 == map2:
        return True
    return False

print(isIsomorphic("egg", "add"))
print(isIsomorphic("foo", "bar"))

# 219. Contains Duplicate II

def containsNearbyDuplicate(nums, k) -> bool:
    hmap = {}
    for idx in range(len(nums)):
        if nums[idx] in hmap and abs(idx - hmap[nums[idx]]) <= k:
            return True
        hmap[nums[idx]] = idx
    return False

print(containsNearbyDuplicate([1,2,3,1], 3))
print(containsNearbyDuplicate([1,2,3,1,2,3], 2))


# 434. Number of Segments in a String

def countSegments(s) -> int:
    count = 0
    for i in range(len(s)):
        if s[i] != ' ' and (i == 0 or s[i-1] == ' '):
            count += 1
    return count

print(countSegments("Hello, my name is John")) # 5

# 441. Arranging Coins

def arrangeCoins(n) -> int:
    i=0
    while n >= 0:
        i += 1
        n = n - i
    return i - 1

print(arrangeCoins(5)) #2


# 231. Power of Two

def isPowerOfTwo(n) -> bool:
    return n > 0 and n&(n - 1) == 0

print(isPowerOfTwo(16)) # True
print(isPowerOfTwo(3)) # Flase

# 258. Add Digits

def addDigits(num) -> int:
    while num > 9:
        sum_num = 0
        while num:
            sum_num += num % 10
            num = num // 10
        num = sum_num
    return num

print(addDigits(38)) #2

# 459. Repeated Substring Pattern

def repeatedSubstringPattern(s) -> bool:
    return s in s[1:] + s[:-1]

print(repeatedSubstringPattern('xyxyxy'))
print(repeatedSubstringPattern('xyx'))


# 645. Set Mismatch
def findErrorNums(nums):
    l = len(nums)
    m = l * (l + 1) // 2
    miss = m - sum(set(nums))
    dup = sum(nums) + miss - m
    return [dup, miss]

print(findErrorNums([1,2,2,3,4]))
print(findErrorNums([1,2,3,4,5,5,6]))


# 653. Two Sum IV - Input is a BST

def findTarget(root, k) -> bool:
    values = {}
    def _findTarget(node):
        if not node:
            return False
        if node.val in values:
            return True
        values[k - node.val] = True
        return _findTarget(node.left) or _findTarget(node.right)
    return _findTarget(root)

# 606. Construct String from Binary Tree

def tree2str(root) -> str:
    if root is None:
        return ''
    s = str(root.val)
    if root.left is None and root.right is None:
        s += ''
    if root.left:
        s += '({})'.format(tree2str(root.left))
    if root.left is None and root.right:
        s += '()'
    if root.right:
        s += '({})'.format(tree2str(root.right))
    return s

# 872. Leaf-Similar Trees

def leafSimilar(root1, root2) -> bool:
    def dfs(root):
        if not root: return []
        if not root.left and not root.right:
            return [root.val]
        return dfs(root.left) + dfs(root.right)
    return dfs(root1) == dfs(root2)


# 2. Add Two Numbers

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = current = ListNode(0)
    carry = 0
    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next
        current.next = ListNode(carry % 10)
        current = current.next
        carry //= 10
    return dummy.next

# 1. Two Sum

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    dictionary = {}
    for i, num in enumerate(nums):
        if num in dictionary:
            return [dictionary[num], i]
        dictionary[target - num] = i

print(twoSum([2,7,11,15], 9))

# 20. Valid Parentheses

def isValid(s) -> bool:
    parens = {
    "{" : "}",
    "[" : "]",
    "(" : ")"
    }
    stack = []
    for char in s:
        if char in parens:
            stack.append(char)
        elif len(stack) == 0 or parens[stack[-1]] != char:
            return False
        else:
            stack.pop()
    return len(stack) == 0

print(isValid("()[]{}"))


# 141. Linked List Cycle

def hasCycle(head) -> bool:
    visited = set()
    current = head

    while current is not None:
        if current in visited:
            return True
        visited.add(current)
        current = current.next
    return False

# 144. Binary Tree Preorder Traversal

def preorderTraversal(root):
    def dfs(node):
        if node is None:
            return []
        res.append(node.val)
        dfs(node.left)
        dfs(node.right)
    res = []
    dfs(root)
    return res

# 145. Binary Tree Postorder Traversal

def postorder_traversal(root) -> list:
    if root is None:
        return []
    res = []
    stack = [root]
    while stack:
        current = stack.pop()
        res.append(current.val)
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
    return res[::-1]

# 35. Search Insert Position

def searchInsert(nums, target) -> int:
    low, high = 0, len(nums)
    while low < high:
        mid = (low + high)//2
        if target > nums[mid]:
            low = mid + 1
        else:
            high = mid
    return low


# 58. Length of Last Word

def lengthOfLastWord(s: str) -> int:
    words = s.split()
    if words:
        return len(words[-1])
    return 0

# 21. Merge Two Sorted Lists

def mergeTwoLists(list1, list2):
    dummy = ListNode()
    cur = dummy
    while list1 and list2:
        if list1.val <= list2.val:
            cur.next = list1
            list1 = list1.next
        else:
            cur.next = list2
            list2 = list2.next
        cur = cur.next
    cur.next = list1 or list2
    return dummy.next

# 28. Find the Index of the First Occurrence in a String

def strStr(haystack: str, needle: str) -> int:
    return haystack.find(needle)

print(strStr("sadbutsad", "sad"))