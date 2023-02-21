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
