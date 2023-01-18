"""DS&A 1"""
# 217. Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


def containsDuplicate( nums ) -> bool:
    count = {}
    for num in nums:
        if num not in count:
            count[num] = 0
        count[num] += 1
        if count[num] > 1:
            return True
        
    return False

print(containsDuplicate([1,2,3,1]))
print(containsDuplicate([1,2,3]))   

# better answer:

def containsDuplicate2(nums) -> bool:
    unique = set(nums)
    if len(unique) < len(nums):
        return True
    return False


print(containsDuplicate2([1,2,3,1]))
print(containsDuplicate2([1,2,3]))



# Max Value

def max_value(nums):
  max = float('-inf')
  for num in nums:
    if num > max:
      max = num
  return max
    
print(max_value([4, 7, 2, 8, 10, 9]))
print(max_value([10, 5, 40, 40.3]))
print(max_value([-5, -2, -1, -11]))




# Is Prime

from math import sqrt, floor
def is_prime(n):
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

def uncompress(s):
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

def compress(s):
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