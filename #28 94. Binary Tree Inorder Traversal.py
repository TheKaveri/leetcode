from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# If we have an empty tree, we add nothing to the list.
# If we have to traverse a a non-empty tree:
# 1. traverse the left sub-tree
# 2. add the root to the list
# 3. traverse the right sub-tree

def in_order_traversal(root: Optional[TreeNode]) -> list[int]:
    accumulator = []
    helper(root, accumulator)
    return accumulator

def helper(root: Optional[TreeNode], acc: list[int]) -> None:
    if root is None:
        return
    helper(root.left, acc)
    acc.append(root.val)
    helper(root.right, acc)

# This takes O(n) time and O(h) space.
# n -> TreeNode count, h -> Tree height

# Here's an implementation with lesser lines of code:
def in_order_traversal(root: Optional[TreeNode]) -> list[int]:
    result = []
    if root:
        result += in_order_traversal(root.left)
        result.append(root.val)
        result += in_order_traversal(root.right)
    return result

# Here's an iterative implementation that simulates
# the call stack:
# https://www.youtube.com/watch?v=g_S5WuasWUE
def in_order_traversal(root: Optional[TreeNode]) -> list[int]:
    res = []
    stack = []
    curr = root

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr.val)
        curr = curr.right
    
    return res