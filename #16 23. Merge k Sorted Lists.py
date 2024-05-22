from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Idea:
# Let's first simplify the problem and try to solve merging
# two sorted linked-lists into one big sorted linked-list.

def merge_2_lists(list1: ListNode, list2: ListNode) -> ListNode:
    merged_list = ListNode(-1) # dummy node
    tail = merged_list

    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
             tail.next = list2
             list2 = list2.next
        tail = tail.next
    
    if list1:
         tail.next = list1

    if list2:
         tail.next = list2
        
    return merged_list.next # to clear the dummy node

# This takes O(n + m) time and O(1) extra space. Where
# n is the count of ListNodes in list1 and m the count of
# ListNodes in list2.

# Since we can merge 2 linked-lists using the merge_2_lists
# function. We can iterate over 'lists' and and merge all the
# linked-lists one by one to a single accumulator.

def merge_k_lists(lists: list[Optional[ListNode]]) -> Optional[ListNode]:
    accumulator = None

    for list in lists:
        accumulator = merge_2_lists(accumulator, list)
    
    return accumulator

# For simplicity, if:
# k is the len(lists) -> total number of linked-lists
# c is the len(lists[i]) for all i -> the length for each linked-list
# then, 'merge_k_lists' takes O(k * c) time and O(1) extra space.

# Is there a better way to do this?
# Try divide and conquer.

def merge_k_lists(lists: list[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists:
        return None
    elif len(lists) == 1:
        return lists[0]
    elif len(lists) == 2:
        return merge_2_lists(list1=lists[0], list2=lists[1])
    else: # len(lists) > 2
        middle = len(lists) // 2
        # Creates new a copy of the array but still
        # stores the same references to the linked-lists.
        left_half = lists[:middle]
        right_half = lists[middle:]

        merged_left_half = merge_k_lists(left_half)
        merged_right_half = merge_k_lists(right_half)

        accumulator = merge_2_lists(merged_left_half, merged_right_half)

        return accumulator

# Let's find the time complexity of this one.
# Assume k different linked-lists each of length c.
# (i.e. k = len(lists) and c = len(lists[i]) for all i)
# Note that we have k * c distinct ListNodes.

# If it takes T(k) time to merge 'lists', then it 
# takes roughly T(k/2) time to merge it's two halves
# 'left_half' and 'right_half'.

# Each merged halves (i.e. merged_left_half and merged_right_half) 
# will have (k * c) / 2 ListNodes in them since 'lists' has (k * c)
# ListNodes. Hence, it'll take  O(kc/2 + kc/2) = O(kc) time to merge 
# the two halves.

# Therefore:
# T(k) = Θ(1), if k <= 2
# T(k) = 2 * T(k/2) + k * c, if k > 2 where c is the constant.

# By Master's Theorem:
# T(k) = k * log(k) is the time complexity and we take O(logk) extra
# space due to recursion.

# Phew! First ever Leetcode hard problem done. YAY :)