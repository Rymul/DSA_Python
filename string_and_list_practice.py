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
