# This question just asks for a direct
# implementation of the binary search technique.

# Here's an iterative implementation:
def binary_search(nums: list[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        while start <= end:
            # while there is a valid search space
            mid = (start + end) // 2

            if nums[mid] < target:
                # search right half
                start = mid + 1
            elif target < nums[mid]:
                # search left half
                end = mid - 1
            else:
                # nums[mid] == target
                return mid
        return -1

# Time: O(logn), Extra space: O(1)

# Here's a recursive implementation:
def binary_search(nums: list[int], target: int) -> int:
     return binary_search_recursive(nums, target, 0, len(nums) - 1)

def binary_search_recursive(nums: list[int], target: int, start: int, end: int) -> int:
    if start > end:
        # not a valid search space
        return -1

    mid = (start + end) // 2

    if nums[mid] < target:
        # search the right half
        return binary_search_recursive(nums, target, mid + 1, end)
    elif target < nums[mid]:
        # search the left half
        return binary_search_recursive(nums, target, start, mid - 1)
    else:
        # nums[mid] == target
        return mid

# Time: O(logn), Extra space: O(logn)

# The recursive solution seems more intuitive.