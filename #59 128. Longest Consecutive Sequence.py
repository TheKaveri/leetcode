# The existence of duplicates in nums
# to not change the answer, so if there
# are any duplicates we rid them.

# Let's try to do an O(nlogn) solution
from collections import defaultdict


def longest_consecutive(nums: list[int]) -> int:
    if not nums:
        return 0
    
    nums = list(set(nums)) # O(n)
    nums.sort()

    # { lengths = []; length = 1 }
    lengths = [1]

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] + 1:
            # { length += 1 }
            lengths[-1] += 1
        else:
            # { lengths.append(length); length = 1 }
            lengths.append(1)
    # { lengths.append(length) }
    return max(lengths)

# Let's try O(n) solution
def longest_consecutive(nums: list[int]) -> int:
    if not nums:
        return 0
    
    nums = set(nums)
    max_length = 0
    cache = {}
    for elem in nums:
        # { lengths.append(helper(hashset, elem)) }
        length = helper_memo(nums, elem, cache)
        max_length = max(max_length, length)

    return max_length

# 'helper' gives the length of the longest consecutive
# sequence of numbers in 'hashset' that begin with
# 'elem'.
# Note: 'elem' is guaranteed to exist in 'hashset'

# This is naive recursion. Let's try to memoize.
def helper(hashset, elem) -> int:
    if elem + 1 not in hashset:
        return 1
    else:
        # elem + 1 is in hashset
        return 1 + helper(hashset, elem + 1)
    
# Memoized version:
# cache[elem] -> helper(hashset, elem)
def helper_memo(hashset, elem, cache) -> int:
    if elem + 1 not in hashset:
        return 1
    elif elem in cache:
        return cache[elem]
    else:
        cache[elem] = 1 + helper_memo(hashset, elem + 1, cache)
        return cache[elem]
    
# This is probably the most superior method? Credit:
# https://leetcode.com/problems/longest-consecutive-sequence/solutions/41057/simple-o-n-with-explanation-just-walk-each-streak

def longest_consecutive(nums: list[int]) -> int:
    nums = set(nums)
    max_length = 0

    for elem in nums:
        if elem - 1 not in nums:
            # elem is the start of a sequence
            curr = elem
            length = 1
            while curr + 1 in nums:
                length += 1
                curr += 1
            max_length = max(length, max_length)
        else:
            continue

    return max_length