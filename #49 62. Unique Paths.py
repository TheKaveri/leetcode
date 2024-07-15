# Given:

# m -> represents rows
# n -> represents columns

# Let's do this in three different ways:
# 1. Recursion
# 2. Memoization
# 3. Dynamic Programming

# 'helper' returns the number of unique
# paths the robot at (r, c) can take to
# reach (rows - 1, cols - 1).

# If the robot happens to be at a position
# outside the grid, there are exactly zero
# paths to reach the destination.

# If the robot happens to be at the destination
# itself, then there's only one trivial path.
# Eg: r = c = 0 and rows = cols = 1

def unique_paths(m: int, n: int) -> int:
    return helper(0, 0, m, n)
    # OR return memo(0, 0, m, n, {})
    # OR return tabulation(m, n)
    # OR return tabulation_v2(m, n)

def helper(r: int, c: int, rows: int, cols: int) -> int:
     if r >= rows or c >= cols:
         return 0
     elif (r, c) == (rows - 1, cols - 1):
         return 1
     else:
         right_paths = helper(r + 1, c, rows, cols)
         down_paths = helper(r, c + 1, rows, cols)
         return right_paths + down_paths
# Time: O(2^(rows + cols)) -> by analysis of decision tree
# Space: O(rows + cols) -> length of path/ height of decision tree
     
def memo(r: int, c: int, rows: int, cols: int, cache) -> int:
    if r >= rows or c >= cols:
        return 0
    elif (r, c) == (rows - 1, cols - 1):
        return 1
    elif (r, c) in cache:
        return cache[(r, c)]
    else:
        cache[(r, c)] =  memo(r + 1, c, rows, cols, cache) + memo(r, c + 1, rows, cols, cache)
        return cache[(r, c)]
# Time: O(rows * cols) -> since we have to count paths of every cell.
# Space: O(rows * cols) -> since we store values of every cell.

# From base cases, we know that:
# dp[rows][_] = 0
# dp[_][cols] = 0
# dp[rows - 1][cols - 1] = 1

# And finally, dp[r][c] = dp[r + 1][c] + dp[r][c + 1]

def tabulation(rows: int, cols: int) -> int:
    dp = [[0] * (cols + 1) for _ in range(rows + 1)]
    # initalize state space and fill it with some
    # base cases at the same time.

    dp[rows - 1][cols - 1] = 1 # base case

    for r in range(rows - 1, - 1, -1):
        for c in range(cols - 1, -1, -1):
            if not dp[r][c]: # dp[r][c] hasn't been initialized
                dp[r][c] = dp[r + 1][c] + dp[r][c + 1]
    return dp[0][0]
# Time and space: O(rows * cols)

def tabulation_v2(rows: int, cols: int) -> int:
    prev = [0] * (cols + 1) # base case

    curr = [0] * (cols + 1)
    curr[-2] = 1 # base case

    for _ in range(rows - 1, -1, -1):
        for c in range(cols - 1, -1, -1):
            if not curr[c]: # curr[c] hasn't been initialized
                curr[c] = prev[c] + curr[c + 1]
        prev = curr
        curr = [0] * (cols + 1)
    
    return prev[0]
# Time and space: O(rows * cols) and O(cols) respectively