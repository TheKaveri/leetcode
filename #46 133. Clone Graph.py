# Idea:
# We are given a node as a reference in the call,
# the task is to duplicate the entire graph. To do
# so we much build each node and it's edges step by
# step.

# Let's try this by using a hashmap. The hashmap will
# store key-value pairs in the form:
# node.val -> Node(node.val)

# i.e. hashmap[1] gives the actual node from Node class
# associated with the value 1.

from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def clone_graph(node: Optional['Node']) -> Optional['Node']:
    if node is None:
        return None
    
    hashmap = {}
    build_graph(node, hashmap)

    return hashmap[node.val]

def build_graph(node: Optional['Node'], hashmap) -> None:
    if node.val not in hashmap:
        hashmap[node.val] = Node(node.val)
        for neighbor in node.neighbors:
            build_graph(neighbor, hashmap) # guarantees that
            # neighbor is in the hashmap
            neighbor_node = hashmap[neighbor.val]
            hashmap[node.val].neighbors.append(neighbor_node)
    else:
        return
    
# Time Complexity: O(V + E)
# Space Complexity: O(V)

# One can also map the old node to the new node
# instead of mapping node.val to the new node.