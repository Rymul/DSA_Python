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

