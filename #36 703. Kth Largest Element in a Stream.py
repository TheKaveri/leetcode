import heapq

# We are given to to find the kth largest element
# in the sorted order from a stream, not the kth
# distinct. This means that if we were to store
# the stream, duplicates should be allowed.

# I'll try an easy implementation using arrays
# and later on try with heaps/priority-queues.

class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.position = k
        self.stream = sorted(nums)

    def add(self, val: int) -> int:
        self.stream.append(val)
        self.stream.sort()
        return self.stream[-self.position]
    # Add takes O(nlogn) time
    
# Another implementation using arrays:
class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.position = k
        self.stream = sorted(nums)

    def add(self, val: int) -> int:
        for i in range(len(self.stream)):
            if self.stream[i] >= val:
                self.stream.insert(i, val)
                break
        else:
            self.stream.append(val)
        return self.stream[-self.position]
    # Add takes O(n) time

# Let's implement using heaps/priority-queues.
# Couldn't solve it by myself so here's a video
# explaining it:
# https://www.youtube.com/watch?v=hOjcdrqMoQ8

class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        # min_heap with largest k elements
        self.min_heap, self.k = nums, k
        heapq.heapify(self.min_heap)
        # this converts the list into a heap in O(n) time

        while len(self.min_heap > k):
            heapq.heappop(self.min_heap)
    
    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0] # contains the min element
