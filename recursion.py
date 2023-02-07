# Recursive Subsets

def subsets(elements):
    """Returns a 2D list where each sublist represents one of the possible subsets of the list"""
    if len(elements) == 0:
        return [[]]
    first = elements[0]
    subs_without_first = subsets(elements[1:])
    subs_with_first = []
    for sub in subs_without_first:
        subs_with_first.append([first, *sub])
    return subs_with_first + subs_without_first

print(subsets(['a', 'b', 'c', 'd']))
print(subsets(['a', 'b', 'c', 'd', 'e', 'f']))

# Permutations

def permutations(items):
    """Returns a 2d list of all possible permutations"""
    if len(items) == 0:
        return [[]]
    first = items[0]
    res = []
    for perm in permutations(items[1:]):
        for i in range(len(perm) + 1):
            res.append(perm[:i] + [first] + perm[i:])
    return res

print(permutations(['cat', 'dog']))
print(permutations(['cat', 'dog', 'cow', 'duck']))
print(permutations([1,2,3,4,5,6]))
