def paired_parentheses(string) -> bool:
    """Returns a boolean indicating if the string has well formated parentheses"""
    count = 0
    for char in string:
        if char == '(':
            count += 1
        if char == ')':
            if count == 0:
                return False
            count -= 1
    return count == 0

print(paired_parentheses("(david)((abby))")) # True
print(paired_parentheses(")(")) # False
