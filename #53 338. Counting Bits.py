# This question basically asks to find the
# hamming weight of a list of contiguous numbers.
# https://en.wikipedia.org/wiki/Hamming_weight#/media/File:Hamming_weight_plot.png

# I drew a binary representation of numbers
# 0 to 16 to find some insight.

# Note: ans[i] -> number of 1 bits in the 
# binary representation of 'i'.

# 1. If 'i' is odd, then last bit is one. To rid this
# last bit, we can do: i >> 1. Hence we can say:
# ans[i] = 1 + ans[i >> 1]

# 2. If 'i' is even, then the last bit is zero. So the
# following statement is true:
# ans[i] = ans[i >> 1]

# The following case is also true:
# ans[i] = 1 if 'i' is of the form
# 2 raised to some power 'm' where m >= 0.
# However, this is a corollary of the 2nd case.

# This question now seems like a DP problem with our
# base case:
# ans[0] = 0

def count_bits(n: int) -> list[int]:
    dp = [0] * (n + 1)
    # initialize state space and base-case

    for i in range(1, n + 1):
        if i % 2 == 1:
            dp[i] = 1 + dp[i >> 1]
        else:
            dp[i] = dp[i >> 1]
    return dp

# Time complexity: O(n)
# Extra-space complexity: O(1) -> nothing extra is created

# More concise solution:
def count_bits(n: int) -> list[int]:
    dp = [0] * (n + 1)
    # initialize state space and base-case

    for i in range(1, n + 1):
        dp[i] = dp[i >> 1] + (i & 1)
    return dp