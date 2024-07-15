# Please read '#49 62. Unique Paths.py' before
# attempting this one.

# This is quite similar to the original unique
# paths problem. The only difference is that
# we need to take care of the obstacles. All
# other base-cases are similar.

def unique_paths_with_obstacles(obstacle_grid: list[list[int]]) -> int:
    return helper(0, 0, obstacle_grid)
    # OR return memo(0, 0, obstacle_grid, {})
    # OR tabulation(obstacle_grid)
    # OR tabulation_v2(obstacle_grid)

# Since we move only down or right, we won't visit 
# a cell twice during the construction of a single path.
# This eliminates the need for a 'visited' set.

# Note: We might have two different paths that have 
# common cells.

# If the robot happens to stand on an obstacle
# there's zero valid paths to the destination
# as cells that are obstacles cannot belong to
# the path.

# 'helper' returns the number of unique paths
# the robot can take from (r, c) to the grid's
# bottom-right corner.

def helper(r, c, obstacle_grid) -> int:
    ROWS, COLS = len(obstacle_grid), len(obstacle_grid[0])
    if r >= ROWS or c >= COLS or obstacle_grid[r][c] == 1:
        return 0
    elif (r, c) == (ROWS - 1, COLS - 1):
        return 1
    else:
        return helper(r + 1, c, obstacle_grid) + helper(r, c + 1, obstacle_grid)
    
# Let's memoize:
def memo(r, c, obstacle_grid, cache) -> int:
    ROWS, COLS = len(obstacle_grid), len(obstacle_grid[0])
    if r == ROWS or c == COLS or obstacle_grid[r][c] == 1:
        return 0
    elif (r, c) == (ROWS - 1, COLS - 1):
        return 1
    elif (r, c) in cache:
        return cache[(r, c)]
    else:
        cache[(r, c)] = memo(r + 1, c, obstacle_grid, cache) + memo(r, c + 1, obstacle_grid, cache)
        return cache[(r, c)]

# Let's try tabulation now. Once again,
# this is quite similar to the original
# unique paths problem. The only difference
# is the additional base-case.

# From base cases, we know that:
# 1. dp[rows][_] = 0
# 2. dp[_][cols] = 0
# 3. dp[rows - 1][cols - 1] = 1
# 4. dp[r][c] = 0 iff obstacle_grid[r][c] == 0
# i.e. there is an obstacle at (r, c)

# And finally, dp[r][c] = dp[r + 1][c] + dp[r][c + 1] only if
# there's no obstacle at (r, c) 

# There's also a case where there's an obstacle
# at the destination. If that's the case,
# we return zero.

def tabulation(obstacle_grid) -> int:
    ROWS, COLS = len(obstacle_grid), len(obstacle_grid[0])
    if (obstacle_grid[ROWS - 1][COLS - 1] == 1):
        return 0

    dp = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
    # initalize state space and fill it with some
    # base cases at the same time.

    dp[ROWS - 1][COLS - 1] = 1 # base case

    for r in range(ROWS - 1, -1, -1):
        for c in range(COLS - 1, -1, -1):
            if not dp[r][c] and obstacle_grid[r][c] != 1:
                # dp[r][c] hasn't been initialized and
                # there's no obstacle at (r, c)
                dp[r][c] = dp[r + 1][c] + dp[r][c + 1]
    return dp[0][0]

def tabulation_v2(obstacle_grid) -> int:
    ROWS, COLS = len(obstacle_grid), len(obstacle_grid[0])
    if (obstacle_grid[ROWS - 1][COLS - 1] == 1):
        return 0

    prev = [0] * (COLS + 1) # base case

    curr = [0] * (COLS + 1)
    curr[-2] = 1 # base case

    for r in range(ROWS - 1, -1, -1):
        for c in range(COLS - 1, -1, -1):
            if not curr[c] and obstacle_grid[r][c] != 1:
                # curr[c] hasn't been initialized and
                # there's no obstacle at (r, c)
                curr[c] = prev[c] + curr[c + 1]
        prev = curr
        curr = [0] * (COLS + 1)
    return prev[0]

# Since the time and space complexities are identical
# to the ones in the original unique paths problem
# I have not included them here.