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