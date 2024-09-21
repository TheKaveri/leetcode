# Let's solve this without changing the string's
# uppercase letters to lowercase and removing the
# non-alphanumeric characters. We'll do this by
# having two pointers, one at the start and one
# at the end of the string.

# If the character is non-alphanumeric, we just
# ignore it like it's not part of a string.

def is_palindrome(s: str) -> bool:
    start = 0
    end = len(s) - 1

    while start <= end:
        if not s[start].isalnum():
            start += 1
        elif not s[end].isalnum():
            end -= 1
        elif s[start].lower() != s[end].lower():
            return False
        else:
            start += 1
            end -= 1

    return True

# Let's try another approach (possibly suboptimal)

def is_palindrome(s: str) -> bool:
    filtered_s = [c.lower() for c in s if c.isalnum()]
    new_s = "".join(filtered_s)

    return new_s == new_s[::-1]