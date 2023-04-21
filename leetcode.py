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
