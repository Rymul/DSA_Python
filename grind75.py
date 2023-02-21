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
