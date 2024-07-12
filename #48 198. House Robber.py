# Some thoughts:

# I created some examples of the 
# problem for drawing out the recursion
# tree.

# I have decided that the robber goes from
# the left side of array to the right side.

# Here are the generified examples I chose:
# [H4, H3, H2, H1]
# [H5, H4, H3, H2, H1]
# [H7, H6, H5, H4, H3, H2, H1]

# This helped me understand how the growing
# problem breaks down into simpler version. 
# I was also able to see which recursive calls
# are repeated various times in the recursion
# tree.

# We can have the following strategies:

# 1) At each house, we rob the current house
# but also try robbing the all houses to
# it's right, except for the very next house.
# This is brute force.

# OR

# 2) At each house, we rob the current house
# and then try robbing the 2nd and the 3rd house
# to the right. 

# Drawing the recursion tree for both strategies, 
# strategy 1 explores all possible ways one can rob
# but for our problem we don't need that. Since all
# houses have non-negative money-stash, and because
# we need to maximize the stolen cash strategy 2 is 
# sufficient.

# 'rob' gives the maximum amount of we can rob
# without alerting the police.
def rob(nums: list[int]) -> int:
    if not nums:
        return 0
    elif len(nums) <= 2:
        return max(nums)
    
    first_path = nums[0] + rob(nums[2:])
    second_path = nums[1] + rob(nums[3: ])

    return max(first_path, second_path)

# This naive recursive solution exceeds the time
# limit on leetcode. Let's try to memoize it.

# Before that, lets use pointers instead of list
# slices.

def rob(nums: list[int]) -> int:
    def helper(start, end):
        if start > end:
            return 0
        elif end - start + 1 <= 2:
            return max(nums[start: end + 1])
    
        first_path = nums[start] + helper(start + 2, end)
        second_path = nums[start + 1] + helper(start + 3, end)

        return max(first_path, second_path)
    
    return helper(0, len(nums) - 1)

# Now let's memoize it:
def rob(nums: list[int]) -> int:
    def helper(start, end, cache):
        if start > end:
            return 0
        elif end - start + 1 <= 2:
            return max(nums[start: end + 1])
        elif start in cache:
            # cache lookup
            return cache[start]
    
        first_path = nums[start] + helper(start + 2, end, cache)
        second_path = nums[start + 1] + helper(start + 3, end, cache)

        cache[start] = max(first_path, second_path)
        # cache[start] stores the solution for robbing the
        # nums[start: end + 1] sub-array
        return cache[start]
    
    return helper(0, len(nums) - 1, {})

# Time complexity: O(N) where N is len(nums)
# Space complexity: O(N)

# Let's try a bottom-up DP approach.
# Credits for bottom-up: https://www.youtube.com/watch?v=kIII1uT6F8Y (Greg Hogg)

# dp[i] -> gives the max amount that can be robbed 
# from house-0 to house-i. Note: strong induction
# applies for elements from dp[0] to dp[i].

# 1. dp[0] -> max amount we can rob from house-0.
# Hence, dp[0] = nums[0]
# 2. dp[1] -> max amount we can rob from house-0 to
# house-1. We can't rob adjacent houses; so here, we
# can only chose one house.
# Hence, dp[1] = max(nums[0], nums[1])

# 3. Given we have maximally robbed from house-0 to
# house-(j-1), we have to maximally rob from house-0
# to house-j:

# We can either not rob j; in this case we have dp[j - 1]
# cash in hand OR We can chose to rob j; if so we can't
# keep house-(j-1)'s cash since we can't rob adjacent 
# houses. We can maximally rob only up till house-(j-2).
# We proceed to rob till j-2 since we want to maximize 
# the money. Hence we can have atmost nums[j] + dp[j - 2] 
# cash.

# We want maximum of both the scenarios so:
# dp[j] = max( dp[j - 1], nums[j] + dp[j - 2] )

def rob(nums: list[int]) -> int:
    n = len(nums)
    if n == 1:
        return nums[0]
    elif n == 2:
        return max(nums[0], nums[1])
    
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for j in range(2, n):
        dp[j] = max(dp[j - 1], nums[j] + dp[j - 2])
    
    return dp[n - 1] # max amount we can rob
    # from house-0 to house-(n-1)

# Time and space are both O(N).

# Constant-space implementation
# (ugly code in my opinion):
def rob(nums: list[int]) -> int:
    n = len(nums)
    if n == 1:
        return nums[0]
    elif n == 2:
        return max(nums[0], nums[1])
    
    prev = nums[0]
    curr = max(nums[0], nums[1])

    for j in range(2, n):
        prev, curr = curr, max(curr, nums[j] + prev)
    
    return curr