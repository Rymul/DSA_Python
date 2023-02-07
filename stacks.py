# Paird Parentheses

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


# Properly Formatted Brackets

def properly_formatted_brackets(string):
    """Returns a boolean indicating if the string has properly formated brackets"""
    stack = []

    symbols = {
        '(' : ')',
        '[' : ']',
        '{' : '}'
    }
    for char in string:
        if char in symbols:
            stack.append(symbols[char])
        else:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                return False
    return len(stack) == 0

print(properly_formatted_brackets('(){}[](())')) # True
print(properly_formatted_brackets('[]{}(}[]')) # False