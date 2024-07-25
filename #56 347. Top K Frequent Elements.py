# Here's an idea:

# We will use hashmaps to keep track of
# the occurance of each element in nums.

# After that we will convert all the occurance
# values into a heap. This will help us find
# the top k elements.

# We have to take of the fact that the heapq
# module implements a min-heap.

# Generically, hashmap maps type 'elem' to
# type 'occurance'

import heapq
from collections import defaultdict

def top_k_frequent(nums: list[int], k: int) -> list[int]:
    hashmap = defaultdict(int)

    # O(n)
    for num in nums:
        hashmap[num] += 1

    occurances = list(hashmap.values())
    occurances = [-x for x in occurances]
    heapq.heapify(occurances) # O(n)

    answer = []

    # O(n * k)
    for _ in range(k):
        max_occur = -heapq.heappop(occurances)
        for num in hashmap:
            if hashmap[num] == max_occur:
                answer.append(num)
                hashmap[num] = -1

    return answer

# Here's a better solution:
# https://www.youtube.com/watch?v=YPTqKIgVk-k

def top_k_frequent(nums: list[int], k: int) -> list[int]:
    hashmap = defaultdict(int)

    for num in nums:
        hashmap[num] += 1
    
    freqs = [[] for _ in range(len(nums) + 1)]

    for elem, freq in hashmap.items():
        freqs[freq].append(elem)

    result = []

    for i in range(len(freqs) - 1, -1, -1):
        for num in freqs[i]:
            result.append(num)
            if len(result) == k:
                return result
            
# Time is O(n)

print(top_k_frequent(nums = [1,1,1,2,2,3], k = 2))