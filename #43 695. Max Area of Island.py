# I solved Leetcode-200 a while ago
# and this question seems quite similar
# to it. Here's an idea:

# We find a land (which maybe a part of
# an island) on the grid. Then we explore
# it's neighbouring regions to determine
# the area of the island. By traversing
# all connected land tiles, we can
# accurately calculate the total area of
# the island.

# We repeat the land-search until we have
# found the areas of all available islands.

# Then we finally return the area of the
# largest island.

# calc_area finds the area of the entire
# island of which the land, in position 
# (row, col) of grid, is a segment of.
def calc_area(grid, row, col) -> int:
    ROWS, COLS = len(grid), len(grid[0])

    if (row < 0 or col < 0 or row >= ROWS
        or col >= COLS or grid[row][col] == 0):
        return 0
    else:
        # grid[row][col] is 1.
        # We mark it visited so that
        # we don't cound this land-tile
        # once more.
        grid[row][col] = 0
        # marking the spot as zero can send
        # the spot in the if-branch if it
        # happens to be called once more during
        # recursion.
        
        area = 1

        area += calc_area(grid, row, col - 1) #L
        area += calc_area(grid, row - 1, col) #U
        area += calc_area(grid, row, col + 1) #R
        area += calc_area(grid, row + 1, col) #D

        return area

# This procedure takes a grid an returns the
# area of the largest island.
def max_area_of_island(grid: list[list[int]]) -> int:
    max_area = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                area = calc_area(grid, row, col)
                if area > max_area:
                    max_area = area
    return max_area

# Time Complexity (worst case):
# O(m * n) since we have to visit the entire
# grid.

# Space Complexity (worst case):
# This happens when the call stack grows
# as much as possible i.e. there is a single
# recursion thread that goes deeper and deeper.

# This can happen if we partially find area of
# all of the cells recursively without popping
# from the call stack in intermediate scenarios.
# Hence O(m * n) is the complexity.

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]

print(max_area_of_island(grid))