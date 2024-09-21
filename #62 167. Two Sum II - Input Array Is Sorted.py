# We are only allowed to use constant extra space. And
# we are guaranteed a unique solution.

# Ex: numbers = [2, 7, 11, 12], target = 23

# We'll start at 2 and search [7, 11, 12] for it's counterpart
# i.e. 23 - 2 = 21. If counterpart is found, then problem is solved.
# Otherwise, we just continue the same idea with the next element.

# Start at 7, and search [11, 12] for 23 - 7 = 16. And so on.

# Note: We don't need to search 'behind' the element. Ex: If are were
# at 11, we don't need to check [2, 7] as well. Because had 2 & 11 formed
# the solution, we would've arrived at it while we searched from 2. Similarly,
# had 7 & 11 formed the solution, we would've arrived at it while we search from
# 7.

def two_sum(numbers: list[int], target: int) -> list[int]:
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]

# Time Complexity is O(n^2) because we look at every possible pair of numbers. 
# The solution also exceeds the time limit on leetcode.

# We can do better than this. 'numbers' is a sorted array
# so we can do binary search instead of linear searching.

def two_sum(numbers: list[int], target: int) -> list[int]:    
    for i in range(len(numbers)):
        counterpart = target - numbers[i]
        # perform binary search for 'counterpart'
        # in the list subsection ahead of i
    
        j = binary_search(counterpart, i + 1, numbers)

        if j != -1:
            # j is valid
            return [i + 1, j + 1]
        
def binary_search(elem, start, nums):
    end = len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if elem == nums[mid]:
            return mid
        elif elem < nums[mid]:
            end = mid - 1
        elif elem > nums[mid]:
            start = mid + 1

    return -1

# Time Complexity is O(nlogn)


# A really good solution: https://www.youtube.com/watch?v=cQ1Oz4ckceM

def two_sum(numbers: list[int], target: int) -> list[int]:
    i = 0
    j = len(numbers) - 1

    while i < j: # can't use same element twice
        targ = numbers[i] + numbers[j]
        if targ < target:
            # must increase sum
            i += 1
        elif targ == target:
            return [i + 1, j + 1]
        elif targ > target:
            # must decrease sum
            j -= 1

# Time Complexity is O(n)

print(two_sum([1,3,4, 5,7,10,11], 9))