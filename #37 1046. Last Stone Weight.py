import heapq

# Since we have to frequently fetch the 
# maximum weighted stones, a max heap
# would be an adequate data structure.

# The 'heapq' Python library only provides
# a min heap. However, we can work around 
# this by negating all the stone weights.
# This will cause the min heap to function
# like a max heap.

def last_stone_weight(stones: list[int]) -> int:
    for i in range(len(stones)):
        stones[i] = - stones[i]
    # negate the stone values

    heapq.heapify(stones)

    while stones:
        # y is the heavier stone.
        y = heapq.heappop(stones)
        if stones:
            x = heapq.heappop(stones)
        else:
            # undo the pop of y
            heapq.heappush(stones, y)
            break

        new_stone = y - x
        if new_stone:
            heapq.heappush(stones, new_stone)
    
    # cancel the negation by negating once more
    return -stones[0] if stones else 0

# In the worst case, for each of the two the pops,
# we push another stone into the heap. So effectively
# thats one pop per iteration. Therefore O(nlogn) is
# the time complexity.

# Here's some better code:
def last_stone_weight(stones: list[int]) -> int:
    for i in range(len(stones)):
        stones[i] = - stones[i]
    # negate the stone values

    heapq.heapify(stones)

    while len(stones) > 1:
        # y is the heavier stone.
        y = heapq.heappop(stones)
        x = heapq.heappop(stones)

        new_stone = y - x
        if new_stone:
            heapq.heappush(stones, new_stone)
    
    if stones:
    # cancel the negation by negating once more
        return -stones[0]
    else:
        return 0

print(last_stone_weight(stones = [2,7,4,1,8,1]))