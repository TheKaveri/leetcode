# Some observations:

# If x is the kth largest element in the array
# then that means that there are k-1 elements
# larger than (or equal to) x.

# So, 1st largest element has 0 elements larger than it.
# Likewise, 3rd largest element has 2 elements larger than it.

# So to find x which is the kth largest element, we can remove
# those k-1 elements larger than it, and return the largest
# element in the array which will be x.

def find_kth_largest(nums: list[int], k: int) -> int: 
    for _ in range(1, k):
        # this loop runs from 1 to k-1
        # i.e. k-1 times
        max_element = max(nums)
        nums.remove(max_element)
    
    kth_largest = max(nums)
    return kth_largest

# k is a constant so this takes O(kn) = O(n) time and O(1) extra
# space.

# Is there a faster method?

# Let's change things a little bit. Instead of finding the kth
# largest element directly consider this: Given an element, what
# largest element is it? (i.e. is it 1st largest, 2nd and so on).
# Let's call that property the rank.

# The lower that rank, the higher the element.

# If we pick the last element (pivot), and apply the quicksort's
# partition algorithm, all elements lesser than the pivot will
# be to it's left and all elements greater than the pivot will
# be to it's right.

# So the rank of that pivot can be easily found by counting the
# number of elements greater than it i.e. in the right sub-section.

# If the pivot's rank is k then the pivot is the kth largest element.
# If the pivot's rank is higher than k, then the kth largest element
# is in the left sub-section.
# If the pivot's rank is lower than k, then the kth largest element
# is in the right sub-section.

# Partitioning puts that pivot in the 'correct place'. 'Correct place'
# means the location the pivot would occupy if the (sub)-array was sorted.

def find_kth_largest(nums: list[int], k: int) -> int: 
    return find_kth_largest_helper(nums, k, 0, len(nums) - 1)

def find_kth_largest_helper(nums: list[int], k: int, start: int, end: int) -> int:
    pivot_index = partition(nums, start, end)

    count_right_section = end - pivot_index
    # Rank is the no. of elements in right sub-section
    # of partition plus one.
    pivot_rank = count_right_section + 1

    if pivot_rank == k:
        return nums[pivot_index]
    elif pivot_rank > k:
        # Pivot is less than the target so
        # the target is in the right half.
        return find_kth_largest_helper(nums, k, pivot_index + 1, end)
    elif pivot_rank < k:
        # Pivot is larger than the target so
        # the target is in the left half.

        # Note that since we discard the right half, the
        # ranks of the elements in the new sub-array changes.
        return find_kth_largest_helper(nums, k - pivot_rank, start, pivot_index - 1)
    
def partition(nums: list[int], start: int, end: int) -> int:
    pivot = nums[end]
    partition_index = start

    for i in range(start, end):
        if nums[i] <= pivot:
            nums[i], nums[partition_index] = nums[partition_index], nums[i]
            partition_index += 1

    nums[end], nums[partition_index] = nums[partition_index], nums[end]

    return partition_index

# Time complexity:
# This is a one branch recursion so average case it is O(n) and worst
# case is O(n^2). Extra space is O(1)

# To understand quickselect test it by hand on different inputs.