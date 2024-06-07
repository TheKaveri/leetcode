from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# The given tree is not a BST so we may need to
# explore all root-leaf paths in the worst case.

# Some observations:
# 1. Number of nodes can be zero, in that
# case, we return false.

# 2. Solving the 'hasPathSum' problem for 'targetSum'
# on a binary tree is like solving the 'hasPathSum'
# problem for 'targetSum-root.val' on the binary tree's
# left and right sub-trees. If sufficient if either of them
# return true.
# Note: root.val is the value of the root of the original
# binary tree.

# 3. While applying observation 2. on the example, I infer:
# Given a tree with a single node (which is technically a leaf),
# If root.val == 'targetSum' then we return true.
# Note: root.val is the value of the only node in the single-node
# tree.

def has_path_sum(root: Optional[TreeNode], target_sum: int) -> bool:
    if not root:
        return False
    
    if not root.left and not root.right:
        # the node is a leaf
        return root.val == target_sum
    elif has_path_sum(root.left, target_sum - root.val):
        return True
    elif has_path_sum(root.right, target_sum - root.val):
        return True

# Worst case time complexity: O(n)
# Worst case space complexity: O(h)
# n -> number of tree nodes.
# h -> height of the tree.

# More concise code but less intuitive for me:
def has_path_sum(root: Optional[TreeNode], target_sum: int) -> bool:
    if not root:
        return False
    
    if not root.left and not root.right:
        # the node is a leaf
        return root.val == target_sum
    
    return has_path_sum(root.left, target_sum - root.val) or has_path_sum(root.right, target_sum - root.val)