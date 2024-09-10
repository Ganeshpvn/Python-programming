def isValid(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or stack.pop() != mapping[char]:
                return False
    return not stack
# Test cases
print(isValid("()"))  # True
print(isValid("()[]{}"))  # True
print(isValid("(]"))  # False