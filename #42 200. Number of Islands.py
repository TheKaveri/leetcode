# Just a thought that came to my mind:
# We can search for an island on this grid,
# if we do find an island, we flood it with
# water (this is like turning all the 1s to 0s).
# Once we have done that, we search for another
# island and repeat the flooding until we can't
# find anymore islands. The number of times we
# search and flood will be the 'number of islands'. 


# find_land searches a grid for a land and
# returns it's coordinates in (row, col) form.
def find_land(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "1":
                return (row, col)
    
    return (-1, -1)

# flood_island floods a single island
# by changing them into water. Because of
# how we use flood_islands in num_islands,
# (row, col) represents a land belonging to
# an island.
def flood_island(grid, row, col):
    ROWS, COLS = len(grid), len(grid[0])

    if (row < 0 or col < 0 or row >= ROWS
        or col >= COLS or grid[row][col] == "0"):
        return
    else:
        # grid[row][col] == "1"
        grid[row][col] = "0" # flood it

        # flood the rest
        flood_island(grid, row, col - 1) #L
        flood_island(grid, row - 1, col) #U
        flood_island(grid, row, col + 1) #R
        flood_island(grid, row + 1, col) #D

def num_islands(grid: list[list[str]]) -> int:
    count_islands = 0
    row, col = find_land(grid)

    while (row, col) != (-1, -1):
        flood_island(grid, row, col)
        count_islands += 1
        row, col = find_land(grid)
    
    return count_islands

# Here's a more optimized version:
def num_islands(grid: list[list[str]]) -> int:
    count_islands = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '1':
                flood_island(grid, row, col)
                count_islands += 1
    
    return count_islands

# Time Complexity (worst case):
# O(m * n) since we have to visit the entire
# grid.

# Space Complexity (worst case):
# This happens when the call stack grows
# as much as possible i.e. there is a single
# recursion thread that goes deeper and deeper.

# This can happen if we flood all of the cells
# recursively without popping from the call stack
# in intermediate scenarios. Hence O(m * n) is the
# complexity.

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(num_islands(grid))