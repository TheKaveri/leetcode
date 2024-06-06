from typing import Optional
from collections import deque

# This question just asks for a modified
# implementation of the BFS algorithm.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root: Optional[TreeNode]) -> list[list[int]]:
    queue = deque()
    levels = []

    if root:
        queue.append(root)
    
    while queue:
        level = []
        for _ in range(len(queue)):
            curr = queue.popleft()
            level.append(curr.val)

            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        levels.append(level)
    
    return levels