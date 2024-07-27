# We are given three rules that must
# be followed to maintain validity.
# First, we'll validate each rule step
# by step. Later we'll try to generify
# some of the code. I'll use an array 
# that will function as a hashmap.

from collections import defaultdict


def is_valid_sudoku(board: list[list[str]]) -> bool:    
    # validate rule 1 & 2
    if not (validate(board, "rows") and validate(board, "cols")):
        return False
    
    # validate rule 3
    pairs = {(0, 0), (0, 3), (0, 6), 
             (3, 0), (3, 3), (3, 6),
             (6, 0), (6, 3), (6, 6)}
    for pair in pairs:
        row, col = pair
        if not is_valid_grid(board, row, col):
            return False
        
    return True

def validate(board, dimension):
    n = 9
    frequencies = [0] * (n + 1)

    for i in range(n):
        for j in range(n):
            if dimension == "rows":
                elem = board[i][j]
            elif dimension == "cols":
                elem = board[j][i]

            if elem.isdigit():
                frequencies[int(elem)] += 1
    
        if not is_valid(frequencies):
            return False
        frequencies = [0] * (n + 1)
    
    return True

# checks if the 3x3 grid of board whose
# top left cell is (row, col) is valid.
def is_valid_grid(board, row, col) -> bool:
    n = 9
    frequencies = [0] * (n + 1)

    for r in range(row, row + 3):
        for c in range(col, col + 3):
            elem = board[r][c]
            if elem.isdigit():
                frequencies[int(elem)] += 1
    
    return is_valid(frequencies)
    
def is_valid(frequencies):
    for freq in frequencies:
            if not (freq == 0 or freq == 1):
                return False
    return True

# Phew! We're done. Time complexity is O(1) since
# we have a fixed board.

# This is a lot of code for just one single problem
# tho :/ Here's a much better solution.
# Credit: https://www.youtube.com/watch?v=TjFXEUCMqI8

# Hashmaps can also map to sets. So we don't need to
# create 9 different hashmaps.

# row[key] -> gives a set of all nos that are in row
# number 'key'

# Similar reasoning for col[key] and grid[key]

def is_valid_sudoku(board: list[list[str]]) -> bool:
    row = defaultdict(set)
    col = defaultdict(set)
    grid = defaultdict(set)

    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            elif (board[r][c] in row[r] or
                  board[r][c] in col[c] or
                  board[r][c] in grid[(r // 3, c // 3)]):
                return False
            else:
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                grid[(r // 3, c // 3)].add(board[r][c])

    return True

# Read this GOAT solution:
# https://leetcode.com/problems/valid-sudoku/solutions/15472/shortsimple-java-using-strings