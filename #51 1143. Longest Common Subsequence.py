# It is given that both strings will be of 
# atleast length one.

# Welp, I couldn't solve this on my own. So I used
# these resources:
# https://www.youtube.com/watch?v=ASoaQq66foQ
# https://www.youtube.com/watch?v=sSno9rV8Rhg
# https://en.wikipedia.org/wiki/Longest_common_subsequence (really important)

# Instead of finding the length of LCS, let's think about
# constructing the LCS. If we happen to meet two same characters,
# then both belong to LCS.
# Eg: LCS(XA..., XB...) = X + LCS(A..., B...)
# Here, '+' is the concat operation.

# If we happened to meet two different characters:
# Eg: LCS(XA...,YB...) then for sure, both X and Y can't
# be in the LCS of the original strings. Either X is or
# Y is or neither is a part of LCS. Surely not both by 
# definition of LCS.

# Therefore we have three decompositions:
# 1. Find LCS(A..., YB...)
# 2. Find LCS(XA..., B...)
# 3. Find LCS(A..., B...)

# Our desired result will be the one that yields the
# longest subsequnce.

# Note: We can do away with the third decomposition as it
# will be one of the subproblems of the first and second
# decomposition. Try decomposing 1 and 2!!

# Now we can use this as an analogy to find the length
# of LCS instead of the LCS itself.

# If either of the strings are empty, len(LCS) = 0

def longest_common_subsequence(text1: str, text2: str) -> int:
    def lcs(i, j):
        if i >= len(text1) or j >= len(text2):
            return 0
        elif text1[i] == text2[j]:
            return 1 + lcs(i + 1, j + 1)
        else:
            return max(lcs(i + 1, j), lcs(i, j + 1))
    
    return lcs(0, 0)

# Let's memoize it:
def longest_common_subsequence(text1: str, text2: str) -> int:
    cache = {}
    def lcs(i, j):
        if i >= len(text1) or j >= len(text2):
            return 0
        elif text1[i] == text2[j]:
            cache[(i, j)] = 1 + lcs(i + 1, j + 1)
            return cache[(i, j)]
        elif (i, j) in cache:
            return cache[(i, j)]
        else:
            cache[(i, j)] = max(lcs(i + 1, j), lcs(i, j + 1))
            return cache[(i, j)]
    
    return lcs(0, 0)

# Let's try dp. Here's what the table that's filled with 
# only base cases which are zeroes would look like:

# -------------------------------
# |    | a | b | c | d | e | "" |
# | a  | Z | X | - | - | - |  0 |
# | c  | - | - | Y | - | - |  0 |  
# | e  | - | - | - | - | - |  0 |
# | "" | 0 | 0 | 0 | 0 | 0 |  0 |
# -------------------------------

# Here, X would mean len_LCS(ace, bcde).
# Here, Y would mean len_LCS(ce, cde).
# Here, Z would mean len_LCS(ace, abcde).

# dp[-1][_] = dp[_][-1] = 0 -> base case
# dp[i][j] = len_LCS of text1[i:] and text2[j:]

# If text1[i] == text2[j]:
# dp[i][j] = 1 + dp[i + 1][j + 1]
# Otherwise:
# dp[i][j] = max of dp[i + 1][j] and dp[i][j + 1]
 
def longest_common_subsequence(text1: str, text2: str) -> int:
    ROWS = len(text1)
    COLS = len(text2)
    dp = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
    # initialize state space and base-cases

    for i in range(ROWS - 1, -1, -1):
        for j in range(COLS - 1, -1, -1):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
    return dp[0][0]
