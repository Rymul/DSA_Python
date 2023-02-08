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
        