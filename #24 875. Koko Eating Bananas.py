import math

# We are given that piles.length <= h i.e.
# the number of hours the guards have gone
# is greater than or equal to the number of
# piles.

# 1 <= piles[i] i.e. there is no 'empty' pile

# In each hour, she eats k bananas from a pile.
# If the pile becomes empty, then she eats from
# the adjacent pile the very next hour.

# Given an eating speed, we can determine whether or
# not Koko can finish the entire pile using 'can_finish'. 

def can_finish_naive(piles: list[int], h: int, speed: int) -> bool:
    # works for any speed values, including negatives.  
    i = 0
    for _ in range(h):
        piles[i] = max(0, piles[i] - speed)
        if not piles[i]:
            i += 1
        if i == len(piles):
            break # can actually return true here.
    
    for pile in piles:
        if pile:
            return False
    return True

# This 'can_finish' implementation can take so much time to finish.
# Try for piles = [312884470] and h = 312884469. When we reach speeds
# around 4, there is so much time taken.

def can_finish(piles: list[int], h: int, speed: int) -> bool:
    if speed <= 0:
        return False
    
    total_hours = 0
    for pile in piles:
        hours_to_finish_pile = math.ceil(pile / speed)
        total_hours += hours_to_finish_pile
    
    if total_hours <= h:
        return True
    else:
        return False

# We can now use 'can_finish' as a function of the variable
# 'k' and use binary search to find the minimum 'k' that satisfies
# 'can_finish'. 'k' as given is the speed of Koko eating bananas.

# If an eating speed satisfies 'can_finish', then we check if its the
# minimum speed that satisfies 'can_finish'.

# If an eating speed doesn't satisfy 'can_finish', then Koko needs to
# eat faster.

def min_eating_speed(piles: list[int], h: int) -> int:
    start, end = 1, max(piles)

    while start <= end:
        mid = (start + end) // 2

        if can_finish(piles, h, speed=mid):
            if can_finish(piles, h, speed=mid - 1):
                # mid is not the min speed
                end = mid - 1
            else:
                # mid is the min speed
                return mid
        else:
            start = mid + 1

# The search itself takes O(logn) where n is the size of the range time
# but the 'can_finish' evaluation takes O(k) where k is the number of piles
# So overall we have O(klogn)

# Here's a better implementation:
# Video: https://www.youtube.com/watch?v=U2SozAs9RzA

def min_eating_speed(piles: list[int], h: int) -> int:
    left, right = 1, max(piles)
    result = right

    while left <= right:
        mid = (left + right) // 2

        total_hours = 0
        for pile in piles:
            total_hours += math.ceil(pile / mid)
        
        if total_hours > h:
            # Koko needs to eat faster
            left = mid + 1
        else:
            # total_hours <= h
            # Update result and check if
            # Koko can eat slower
            result = min(result, mid)
            right = mid - 1

    return result