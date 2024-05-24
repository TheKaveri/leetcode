# Ignoring the unimportant part of the problem,
# at it's core, the question gives a list of
# 0s, 1s and 2s, which need to be sorted in
# ascending order. Since we know the range values
# the list elements take and given such a small range,
# we can use bucket sort.

# Bucket sort is in-place and so it meets the given
# problem constraint.

def sort_colors(nums: list[int]) -> None:
    bucket = [0, 0, 0]

    for colour in nums:
        bucket[colour] += 1
    
    i = 0
    for colour in range(len(bucket)):
        while bucket[colour]:
            nums[i] = colour
            i += 1
            bucket[colour] -= 1

# This takes O(n) time and O(1) extra space.