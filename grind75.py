from collections import Counter

#1. Two Sum

def twoSum(nums, target):
    dictionary = {}
    for i, num in enumerate(nums):
        if num in dictionary:
            return [dictionary[num], i]
        dictionary[target - num] = i
 
n = [2,7,11,15]
t = 9
print(twoSum(n, t))


#20. Valid Parentheses

def isValidParens(s):
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

s1 = "()[]{}"
s2 = "(]"
print(isValidParens(s1))
print(isValidParens(s2))


#21 Merge 2 Sorted Lists

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    dummy = ListNode()
    current = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    current.next = l1 or l2
    return dummy.next


def maxProfit(prices):
    if not prices:
        return 0
    min_buy = prices[0]
    max_profit = 0
    for price in prices:
        max_profit = max(price - min_buy, max_profit)
        if price < min_buy:
            min_buy = price
    return max_profit

p = [7,1,5,3,6,4] # 5
p2 = [7,6,4,3,1] # 0

print(maxProfit(p))
print(maxProfit(p2))

#125 Valid Palindrome

def isPalindrome(str):
    mod_str = (''.join(char for char in str if char.isalnum())).lower()
    return mod_str == mod_str[::-1]

s1 = "A man, a plan, a canal: Panama"
s2 = "race a car"
print(isPalindrome(s1)) # True
print(isPalindrome(s2)) # False

#226. Invert Binary Tree

def invertTree(self, root):
    self.traverseTree(root)
    return root

def traverseTree(self, node):
    if node is None:
        return None
    temp = node.right
    node.right = node.left
    node.left = temp
    self.traverseTree(node.left)
    self.traverseTree(node.right)

#242 Valid Anagram

def isAnagram(s, t):
    return Counter(s) == Counter(t)

s = "anagram"
t = "nagaram"
u = "rat"
v = "cat"
print(isAnagram(s, t)) # True
print(isAnagram(u, v)) # False

#704. Binary Search

def search(nums, target):
    left = 0
    right = len(nums) -1
    while left <= right:
        mid = left + (right-left)//2
        if nums[mid] > target:
            right = mid -1
        elif nums[mid] < target:
            left = mid +1
        else:
            return mid
    return -1

n = [-1,0,3,5,9,12]
t = 9
print(search(n, t)) # 4


#733. Flood Fill

def floodFill( image, sr, sc, color):
    if image[sr][sc] == color:
        return
    fill(image, sr, sc, color, image[sr][sc])
    return image

def fill( image, sr, sc, color, cur):
    if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image):
        return
    if cur != image[sr][sc]:
        return
    image[sr][sc] = color
    fill(image, sr-1, sc, color, cur)
    fill(image, sr+1, sc, color, cur)
    fill(image, sr, sc-1, color, cur)
    fill(image, sr, sc+1, color, cur)

i = [[1,1,1],[1,1,0],[1,0,1]]
sr1 = 1
sc1 = 1
c = 2

print(floodFill(i, sr1, sc1, c))
