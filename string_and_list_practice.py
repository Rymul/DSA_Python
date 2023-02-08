from collections import Counter

def uncompress(s):
    i = 0
    j = 0
    nums = '123456789'
    res = []

    while j < len(s):
        if s[j] in nums:
            j += 1
        else:
            n = int(s[i:j])
            res.append(n * s[j])
            j += 1
            i = j
    return ''.join(res)

print(uncompress("3n12e2z"))


def compress(s):
    i = 0
    j = 0
    s += '!'
    res = []

    while j < len(s):
        if s[j] == s[i]:
            j += 1
        else:
            num = j - i
            if num == 1:
                res.append(s[i])
            else:
                res.append(str(num))
                res.append(s[i])
            i = j
    return ''.join(res)

print(compress('ccaaatsss'))

def anagrams(s1, s2):
    return char_count(s1) == char_count(s2)

def char_count(s):
    count = {}
    for char in s:
        if char not in count:
            count[char] = 0
        count[char] += 1
    return count

print(anagrams('monkeyswrite', 'newyorktimes'))

def better_anagrams(s1, s2):
    return Counter(s1) == Counter(s2)

print(better_anagrams('monkeyswrite', 'newyorktimes'))


def most_frequent_char(s):
    count = Counter(s)
    most = None
    for char in s:
        if most is None or count[char] > count[most]:
            most = char
    return most

print(most_frequent_char('eleventennine'))


def pair_sum(nums, target):
    prev_nums = {}
    for i, n in enumerate(nums):
        comp = target - n
        if comp in prev_nums:
            return (i, prev_nums[comp])
        prev_nums[n] = i

print(pair_sum([4, 7, 9, 2, 5, 1], 3))

def pair_product(numbers, target):
    prev_nums = {}
    for i, num in enumerate(numbers):
        comp = target / num
        if comp in prev_nums:
            return (i, prev_nums[comp])
        prev_nums[num] = i

print(pair_product([4, 7, 9, 2, 5, 1], 5))
