# Rule 0: If we have a matching pair, we can simplify
# the problem by discarding that matching pair.
# As a consequence, any valid string can be eventually
# simplified to have zero matching pairs.

# Rule 1: A closing bracket always matches 
# itself to the most recent opening bracket. (Assuming
# a valid entry and considering Rule 0)

# Rule 2: If a closing bracket appears before it's
# opening brackets, the string is always invalid.

# Algorithm:
# Accept all opening brackets. When encountering a
# closing bracket, see if it follows Rule 1. If yes,
# do Rule 0 and continue, otherwise return False.

def is_valid(s: str) -> bool:
    stack = []
    close_map_open = {')': '(', ']': '[', '}': '{'}

    for bracket in s:
        if bracket not in close_map_open:
            # i.e. if bracket is an 'opening bracket'
            stack.append(bracket)
        else:
            # bracket is a 'closing bracket'
            elem = stack.pop() if stack else '#'
            if close_map_open[bracket] != elem:
                return False
    
    return True if not stack else False