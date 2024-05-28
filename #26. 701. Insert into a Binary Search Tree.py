from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

# insert(root, val) -> inserts 'val' in BST named 'root'
# and << returns the updated tree >>.

# 1. If we have an empty tree, create a new TreeNode
# return it.
# 2. If val is lesser than root.val, then insert in LST.
# 3. If val is greater than root.val, then insert in RST.
# 4. We ignore if val == root.val as BST don't allow duplicate
# entries.

# LST -> left sub-tree
# RST -> right sub-tree
# BST -> binary-search tree
def insert_into_bst(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if root is None:
        return TreeNode(val)
    
    if val < root.val:
        # insert_into_bst(root.left, val)
        # is the updated LST.
        root.left = insert_into_bst(root.left, val)
    elif root.val < val:
        # insert_into_bst(root.right, val)
        # is the updated RST.
        root.right = insert_into_bst(root.right, val)
    return root

# If n is the number of nodes:
# This takes O(logn) time and O(logn) space. (For height-balanced BST)
# Worst case is O(n) for both space and time. (Happens for skewed BST)