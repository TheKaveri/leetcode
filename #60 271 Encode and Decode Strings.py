# The encoding step wants us to encode
# a list of strings to a single string.

# Let's try to take each string and concat
# them into a single string but the '@'
# character will act as a separator.

# ["how", "are", "you"] -> "how@are@you"
# Since we can have empty strings:
# ["how", "are", "you", "", ""] -> "how@are@you@@"

# But, we could run into a problem:
# ["how", "are", "you", "@"] -> "how@are@you@@"

# We have to fix this. Encoding must be a one-to-one
# function. Let's try this:

# ["how", "are", "you"] -> "3@how3@are3@you"
# 3 -> length of the string

# ["how", "are", "you", "", ""] -> "3@how3@are3@you0@0@"
# ["how", "are", "you", "@"] -> "3@how3@are3@you1@@"

# ["how", "are", "you", "777@"] -> "3@how3@are3@you4@777@"
# ["how", "are", "you", "2@"] -> "3@how3@are3@you2@2@"

# Note: we need to take care of the case when length is
# represented as two digits.

def encode(strs: list[str]) -> str:
    encoding = ""

    for word in strs:
        encoding += str(len(word)) +  "@" + word

    return encoding

def decode(s: str) -> list[str]:
    strings = []

    i = 0
    while i < len(s):
        j = i
        while s[j] != "@":
            j += 1
        length = int(s[i:j])
        start = j + 1
        strings.append(s[start: start + length])

        i = start + length

    return strings

lst = ["","   ","!@#$%^&*()_+","LongStringWithNoSpaces","Another, String With, Commas"]
enc = encode(lst)
print(decode(enc) == ["","   ","!@#$%^&*()_+","LongStringWithNoSpaces","Another, String With, Commas"])
            