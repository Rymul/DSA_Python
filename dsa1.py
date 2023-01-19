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