# I'll just directly implement the classic sorting
# algorithms I learnt.

def sort_array(nums: list[int]) -> list[int]:
    return merge_sort(nums)

def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    
    middle = len(nums) // 2
    left_half = nums[:middle]
    right_half = nums[middle:]

    sorted_left_half = merge_sort(left_half)
    sorted_right_half = merge_sort(right_half)

    nums = merge_sorted_lists(sorted_left_half, sorted_right_half)

    return nums

def merge_sorted_lists(list1, list2):
    len1 = len(list1)
    len2 = len(list2)

    merged_list = [0] * (len1 + len2)
    i, j, k = 0, 0, 0

    while i < len1 and j < len2:
        if list1[i] <= list2[j]:
            merged_list[k] = list1[i]
            i += 1
        else:
            merged_list[k] = list2[j]
            j += 1
        k += 1
    
    while i < len1:
        merged_list[k] = list1[i]
        i += 1
        k += 1

    while j < len2:
        merged_list[k] = list2[j]
        j += 1
        k += 1
    
    return merged_list


# Insertion sort is an invalid solution to the problem since it's
# time complexity is O(n^2). I'll still put it in here anyway.
def insertion_sort(nums):
    for i in range(1, len(nums)):
        j = i - 1
        while j >= 0 and nums[j] > nums[j + 1]:
            # perform swap
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
            j -= 1
    return nums

# Unfortunately, naive Quick sort isn't valid on leetcode.
# I'll still put it in here anyway.
def quick_sort(nums, start, end):
    if start >= end:
        return
    
    pivot_index = partition(nums, start, end)
    quick_sort(nums, start, pivot_index - 1)
    quick_sort(nums, pivot_index + 1, end)

def partition(nums, start, end):
    pivot = nums[end]

    partition_index = start

    for i in range(start, end):
        # go through each element of
        # the segment except the pivot

        if nums[i] <= pivot:
            nums[i], nums[partition_index] = nums[partition_index], nums[i]
            partition_index += 1
        
    nums[end], nums[partition_index] = nums[partition_index], nums[end]
    
    return partition_index

# Here's a more efficient version of Quick sort
# that uses randomized pivoting
def quick_sort_r(nums, start, end):
    if start >= end:
        return
    
    pivot_index = partition_r(nums, start, end)
    quick_sort(nums, start, pivot_index - 1)
    quick_sort(nums, pivot_index + 1, end)

def partition_r(nums, start, end):
    import random
    random_index = random.randint(start, end)
    nums[random_index], nums[end] = nums[end], nums[random_index]

    return partition(nums, start, end)

# This randomized pivoting will still give
# take O(n^2) with arrays with elements like
# [2,2,2....,2]