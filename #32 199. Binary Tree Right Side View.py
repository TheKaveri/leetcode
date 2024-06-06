from typing import Optional
from collections import deque

# You can't simply start at root,
# keep going right while you collect
# the node values and return that
# collection.

#    1
# /    \
# 2     3
#  \     \ 
#   5    4
#   /
#  7

# Output: [1,3,4,7]

# Idea:
# Go through each level of the tree,
# like we do in BFS but collect only
# the right-most node of each level.
# OR
# Perform BFS but modify the results.

# Known:
# Root is always part of the solution.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def right_side_view(root: Optional[TreeNode]) -> list[int]:
    queue = deque()
    right_side_nodes = []

    if root:
        queue.append(root)
    
    while queue:
        for _ in range(len(queue)):
            curr = queue.popleft()

            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        # after the for loop is over
        # conveniently, curr is always
        # the right most node in each
        # level so we add it to the result.
        right_side_nodes.append(curr.val)
    
    return right_side_nodes