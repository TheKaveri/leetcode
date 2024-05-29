from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

# remove(root, key) -> removes 'key' in BST named 'root'
# and << returns the updated tree >>.

# 1. If we have an empty tree, we give it back.
# 2. If key is lesser than root.val, then we remove from LST.
# 3. If key is greater than root.val, then we remove from RST.
# 4. If key is equal to root.val, then we remove that node.

# LST -> left sub-tree
# RST -> right sub-tree
# BST -> binary-search tree
def delete_node(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    if root is None:
        return None
    
    if key < root.val:
        # delete_node(root.left, key) is
        # the updated LST.
        root.left = delete_node(root.left, key)
    elif root.val < key:
        # delete_node(root.right, key) is
        # the updated RST.
        root.right = delete_node(root.right, key)
    else:
        # key == root.val

        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            # root has two non-empty
            # subtrees
            next_in_order = min_value_node(root.right)
            root.val = next_in_order.val

            # remove(root.right, next_in_order.val)
            # is the updated RST.
            root.right = delete_node(root.right, next_in_order.val)
            # Doing remove(root, next_in_order.val) is not valid.

    return root

# If n is the number of nodes:
# This takes O(logn) time and O(logn) space. (For height-balanced BST)
# Worst case is O(n) for both space and time. (Happens for skewed BST)

def min_value_node(root):
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr