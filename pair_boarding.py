"""
12. Integer to Roman
input number
output is string
problem: convert number into roman numberal
    edge case if number is 1 less, 10 less, or 100
    less than a multiple of 5 (the given roman numeral sybols)
algorithm:
    list: create an list of values that correspond to roman
    numberals as well as edge cases (ex 4, 9, 400,...)
    dictionary: create dict of numbers in above list and corresponding roman numeral symbols
    variables: left_over: keep track of remaning input, res: return string to concatinate symbols
    interate over list, while left_over >= list element
    concatinate dictionary[element] on res and left_over - ele
"""


def int_to_roman(num: int) -> str:
    """Converts the input number into a Roman Numberal"""
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    dictionary = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    left_over = num
    res = ''

    for val in values:
        while left_over >= val:
            res += dictionary[val]
            left_over -= val
    return res

print(int_to_roman(3))
print(int_to_roman(58))
