# Algorithm:
# If the head is None, then I return None
# Now, for the valid cases:

# The logic is to take the terminal node's 'next' and point it
# to it's previous node 'P'. Then repeat the same procedure for
# 'P' i.e. take P's 'next' and point it to it's predecessor.
# Continue likewise until we reach the head node, where we take 
# it's 'next' and assign it to None since head has no predecessor.

# Also, the head of our reverse linked list is the terminal node of
# the original linked list. 

# I used dynamic arrays to implement my first solution as it helped
# me access the previous node in an intuitive way.
# (The 2nd solution is miles better in my opinion)

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None
    
    curr = head
    nodes = [] 
    
    while curr:
        nodes.append(curr)
        curr = curr.next

    for i in range(len(nodes) - 1, -1, -1):
        if i != 0:
            nodes[i].next = nodes[i - 1]
        else:
            nodes[i].next = None
        
    new_head = nodes[-1]
    return new_head

# This takes O(n) time and O(n) space

# But we can do better, we can avoid using dynamic arrays by changing
# our logic a little. Instead of starting with the terminal node, let's
# start at the head itself. Then to each node's 'next' we will assign
# it's predecessor. We will continue to do so until we reach the terminal
# node (which will be the new head). I've used pointers to help me out.

# Note that the head of the original linked lists has None as it's
#  'predecessor'.

# If you find the logic a little confusing, try to draw it out :)

# This solution is much simpler and elegant.
def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev, curr = None, head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    
    return prev # as it is our new head

# This takes O(n) time and O(1) space

# Now, trying a recursive approach. We know:
# reverse [1,2,3,4] = [4] + reverse [1,2,3] and
# reverse [] = [], where '+' is the list concatenation operator.

# This logic is for arrays but we can use it as an analogy to solve
# the problem for linked lists.

def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None
    elif head.next is None: # We have only a single node
        return head
    else:
        reversed_list = remove_tail_node(head)
        reversed_list.next = reverse_list(head)
        return reversed_list

def remove_tail_node(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head

    while curr.next:
        prev = curr
        curr = curr.next

    if prev:
        prev.next = None

    return curr

# Another attempt at finding a recursive solution. Credit for logic:
# https://www.youtube.com/watch?v=D2vI2DNJGd8
# Really really exceptional video, explains recursion theory really well.

def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None
    elif head.next is None:
        return head
    else:
        new_head = reverse_list(head.next)
        front = head.next
        front.next = head
        head.next = None
        return new_head

#  This takes O(n) time and O(n) space