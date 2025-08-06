def is_paired(input_string):
    stack, pairs = [], {')': '(', '}': '{', ']': '['}
    for string in input_string:
        if string in pairs.values(): stack.append(string)
        elif string in pairs:
            if not stack or stack.pop() != pairs[string]: return False
    return not stack
