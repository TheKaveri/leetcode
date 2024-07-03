from collections import deque

# Since we have to find the shortest path,
# this question can be solved using BFS.

# We don't need any sub-routines.

#  The only catch here is that the tile
# neighbours are 8-directionally connected,
# and not 4-directionally.

def shortest_path_binary_matrix(grid: list[list[int]]) -> int:
    if grid[0][0] == 1:
        return -1
    
    ROWS = COLS = len(grid) # since it's an n by n grid

    queue = deque()
    visited = set()
    
    queue.append((0, 0))
    visited.add((0, 0))

    length = 1
    while queue:
        for _ in range(len(queue)):
            (r, c) = queue.popleft()

            if r == ROWS - 1 and c == COLS - 1:
                return length
        
            directions = [[-1 , -1], [-1 , 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
            for dr, dc in directions:
                if (r + dr < 0 or c + dc < 0 or r + dr >= ROWS
                    or c + dc >= COLS or (r + dr, c + dc) in visited
                    or grid[r + dr][c + dc] == 1):
                    continue
                queue.append((r + dr, c + dc))
                print((r + dr, c + dc))
                visited.add((r + dr, c + dc))
        length += 1
    
    return -1

grid = [[1,0,0],
        [1,1,0],
        [1,1,0]]

print(shortest_path_binary_matrix(grid))

# Since this is a standard BFS, time and space
# complexity is O(n^2) and O(n) respectively.

# But leetcode gives a tighter bound of O(n) for
# both time and space.