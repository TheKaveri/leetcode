import heapq

# Let's try to solve this using heaps.

# Idea:
# Convert the list 'nums' into a heap using
# heapq. Since heapq is implements min-heap
# pop from the heap until we have k elements
# left. The next element in highest priority
# is the solution.

def find_kth_largest(nums: list[int], k: int) -> int:
    heapq.heapify(nums)

    while len(nums) > k:
        heapq.heappop(nums)
    
    return nums[0]