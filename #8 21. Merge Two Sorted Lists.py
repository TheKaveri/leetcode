# Algorithm:
# Start by solving the problem for trivial instances
# and then building it up for more complex scenarios.

# If both list1 and list2 are null then we give back null
# If only one of them is null then return the non null list

# If both are non null, then compare both their heads and take
# the minimum valued node. We can recursively do the rest since
# the next step is like another instance of the original problem.

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if not list1 and not list2:
        return None
    elif not list1:
        return list2
    elif not list2:
        return list1
    else: # list1 and list2 are both not null
        if list1.val < list2.val:
            # merged_list = ListNode(list1.val) -> We don't really have to do this
            merged_list = list1 # This is better
            merged_list.next = merge_two_lists(list1.next, list2)
        else:
            # merged_list = ListNode(list2.val) -> We don't really have to do this
            merged_list = list2 # This is better
            merged_list.next = merge_two_lists(list1, list2.next)
        
        return merged_list
    
# Here is an iterative approach:

def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    merged_list = ListNode(-1) # Dummy node
    
    tail = merged_list
    while list1 and list2:
        if list1.val < list2.val:
            # tail.next = ListNode(list1.val) -> We don't really have to do this
            tail.next = list1 # This is better
            list1 = list1.next
        else:
            # tail.next = ListNode(list2.val) -> We don't really have to do this
            tail.next = list1 # This is better
            list2 = list2.next
        tail = tail.next
    
    if not list1:
        tail.next = list2
    else: # i.e. list2 is None
        tail.next = list1

    return merged_list.next # To get rid of the dummy node