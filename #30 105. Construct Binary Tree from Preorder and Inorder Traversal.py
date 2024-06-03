from typing import Optional

# Preorder: ROOT LST RST
# Inorder: LST ROOT RST

# Some observations:
# 1. The first element in the in the 'preorder' array
# is always the root. Call it R.

# 2. Since R is a root, then all elements that
# appear to it's left in the 'inorder' array 
# belong to the it's left sub-tree. Similarly all 
# elements that appear to it's right in the 'inorder'
# array belong to it's right sub-tree.

# 3. If there are X number of elements before R in
# the 'inorder' array then the first X elements after
# R in the 'preorder' array are elements of it's left
# sub-tree.

# 4. Similarly, if there are Y number of elements after
# R in the 'inorder' array then the last Y elements in
# the 'preorder' array are elements of it's right sub-tree.

# All observations are consequences of how we
# define inorder and preorder traversals.

# 5. Finally, since both inorder and preorder traversals
# are recursive in definition, segments of the 'inorder'
# and 'preorder' arrays can be used as arguments to represent
# the left and right sub-trees respectively. This means that all
# the previous observations we described can be applied to the 
# left and right sub-trees.

# The only tricky part is properly getting the array segments
# to represent the left and right sub-trees. But the observations
# can help.

# Since 1 <= preorder.length and 1 <= inorder.length the simplest case
# i.e. base case is for a single node. However when I debugged using the below
# tree as an example, I found that recursive calls to empty sub-trees are being
# made. So it's single node is not quite a base case.
# Note: inorder.length == preorder.length
# Note: preorder and inorder consist of unique values.


inorder = [6, 8, 9, 11, 12, 14, 15, 20, 26, 30, 35]
preorder = [15, 11, 8, 6, 9, 12, 14, 26, 20, 30, 35]
# inorder = [1]
# preorder = [1]
# Let's take this as an example. Tree can be found here:
# https://www.researchgate.net/profile/Piotr-Labedz/publication/337544122/figure/fig3/AS:829481627426827@1574775239682/An-example-of-a-binary-tree.png
# Test and see if the all the observations hold, including
# step 5.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
    # if preorder/inorder is empty, return an empty tree
    if len(preorder) == 0:
        return None
    
    # otheriwe, locate the root
    root_val = preorder[0]
    # search root.val in 'inorder'  
    root_index = inorder.index(root_val)

    # create LST and RST representations
    # by segmeting 'preorder' and 'inorder'
    lst_inorder = inorder[:root_index] 
    lst_preorder = preorder[1:root_index + 1]

    rst_inorder = inorder[root_index + 1:]
    rst_preorder = preorder[root_index + 1:]

    root = TreeNode(root_val)
    # build the LST and RST and assign them to root
    root.left = build_tree(lst_preorder, lst_inorder)
    root.right = build_tree(rst_preorder, rst_inorder)

    # return the root
    return root

# Shorter version:
def build_tree_short(preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
    if len(preorder) == 0:
        return None
    
    root = TreeNode(preorder[0])
    root_index = inorder.index(root.val)

    root.left = build_tree_short(preorder[1:root_index + 1], inorder[:root_index])
    root.right = build_tree_short(preorder[root_index + 1:], inorder[root_index + 1:])
    return root

# We can avoid creating list slices that cost O(n) by using pointers
# in the build_tree function. Here's the code:

def build_tree_ptr(preorder, inorder) -> Optional[TreeNode]:
    return build_tree_helper(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)

def build_tree_helper(preorder, pre_start, pre_end, inorder, in_start, in_end):
    if pre_start > pre_end:
        return None

    root = TreeNode(preorder[pre_start])
    root_index = inorder.index(root.val)
    # This index is not relative to the 'inorder' array
    # segment. It's relative to the entire 'inorder' array.

    # root_index - in_start is the number of elements
    # in the left sub-tree.
    
    root.left = build_tree_helper(preorder, pre_start + 1, pre_start + root_index - in_start, inorder, in_start, root_index - 1)
    root.right = build_tree_helper(preorder, pre_start + root_index - in_start + 1, pre_end, inorder, root_index + 1, in_end)

    return root

root = build_tree_ptr(preorder, inorder)

# Assume n is the number of nodes.
# Extra space is O(n) (which is unavoidable since we build a tree).
# Average time (if we have a balanced tree) is as follows:
# T(n) = O(n) + 2T(n/2)
# i.e. T(n) = O(nlog(n)) by the Master Theorem.

# If tree is skwewed, then T(n) = O(n) + 2T(n-1)
# i.e. T(n) = O(n^2)