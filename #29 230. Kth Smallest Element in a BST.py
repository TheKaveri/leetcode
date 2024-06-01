# We are given that 1 <= k <= n.
# So 'k' is always a valid parameter.
# And there are no 0 node trees.

# Idea:
# Doing in-order traversal on a BST gives a list
# of node values in sorted order. So this can help
# in finding the answer. However, time complexity
# of such an operation is O(n). But we can optimize
# to acheive O(k) time. For small values of n, the
# difference is trivial but for k = 3 and n = 10000,
# this is significant.

# To achieve O(k) time, we have to in-order traverse
# but only partially. This means that we continue
# in-order traversal until we hit some feasible stop
# condition i.e. when we have reached the first 'k'
# elements.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# The naive implementation simply accumulates all
# n elements into a list using in-order and returns
# the elem at k-1 index. I will not be doing that here.

# Here's the optimized implementation that takes
# O(k) space and time:
def kth_smallest(root, k) -> int:
    first_k_elems = []

    in_order(root, k, first_k_elems)
    return first_k_elems[-1]

def in_order(root, k, accumulator) -> None:
        if not root or len(accumulator) == k:
            # len(accumulator) == k takes care
            # of all calls after the kth elem
            # was added.
            return
        in_order(root.left, k, accumulator)
        if len(accumulator) < k:
            # This condition takes care of
            # calls that partially executed
            # beforehand.
            accumulator.append(root.val)
        in_order(root.right, k, accumulator)


# Here's the iterative analogue of that optimized
# implementation. Takes O(k) time and O(1) space.
# Seems better than the recursive implementation.
def kth_smallest(root, k) -> int:
    count = 0
    stack = []
    curr = root

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        count += 1
        if count == k:
            return curr.val
        curr = curr.right

# NOTE: This was my first solution, conceptually it
# seems okay but it's actually wrong. Debug and see
# why! ;)
def in_order_wrong(root, k, accumulator) -> None:
        if not root:
            return 
        in_order_wrong(root.left, k, accumulator)
        accumulator.append(root.val)
        if len(accumulator) == k:
            # stop condition
            return
        in_order_wrong(root.right, k, accumulator)
