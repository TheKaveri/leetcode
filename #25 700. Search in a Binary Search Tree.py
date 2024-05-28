from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

# 'search_bst' works just like a regular BST search except
# that we return the subtree instead of True/False.

# If we have an empty tree, return None.
# If val < root.val, then search in the LST.
# If root.val < val, then search in the RST.
# If val == root.val, then return the root.

# LST -> left sub-tree
# RST -> right sub-tree
# BST -> binary-search tree

def search_bst(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
        return None
    
    if val < root.val:
        return self.search_bst(root.left, val)
    elif root.val < val:
        return self.search_bst(root.right, val)
    else:
        # val == root.val
        return root
    
# If n is the number of nodes:
# This takes O(logn) time on average and O(logn) space on average.
# Worst case is O(n) for both space and time. (Happens for skewed BST).

# Even less lines of code:
def search_bst(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root or val == root.val:
        return root
    if val < root.val:
        return self.search_bst(root.left, val)
    if root.val < val:
        return self.search_bst(root.right, val)