# Some observations:
# It doesn't make sense to change the
# state of the given heights array.

# Given two heights at i and j, with i < j
# the amount of water is W x H
# W = j - i
# H = min(height[i], height[j])

# Brute force:
# Consider all possible containers. O(n^2).
def max_area(height: list[int]) -> int:
    res = -1
    for i in range(len(height)):
        for j in range(len(height)):
            if i != j:
                area = (j - i) * (min(height[i], height[j]))
                res = max(res, area)

    return res

# Observation:
# Given two lines A & B, say we have another line
# C that is in between A & B. Then area formed by
# C & B (or C & A) will not exceed that of A & B
# if C <= min(A, B).

# Why? Think of the W and H parameter for A & B
# as well for C & B (or C & A).

# It may exceed if C > min(A, B)

# min(A, B) -> line with minimum height when
# considering lines A and B.

# Couldn't solve it by my own. Here's some help from a comment on https://www.youtube.com/watch?v=UuiTKBwPgAo:

# "I think a good explanation for why we move pointer with the lower height is because 
# we already have the max area with that height - since it is the lower pointer that 
# means that every other distance that is closer will always be a smaller distance with 
# the same or less height which means smaller area. Therefore we do not need to look at
# every other combination with that pointer."


# "Explanation for equal heights edge case:
# Let's say we are at l, r where H = h[l] = h[r]. The recommendation would be to update both
# l and r. Why? The current computed area is A = H * (r-l). No other combination of h[i] and 
# H s.t l < i < r can result in an area greater than A as the area would always be bounded by A
# i.e. H*(i-l) or H*(r-i) both of which are always smaller than A. Note by the time we reach this
# state of having equal height H, the max area with H as a boundary is either the current area A or
# already computed in a past iteration."

def max_area(height: list[int]) -> int:
    A, B = 0, len(height) - 1
    res = -1
    
    while A < B:
        area = (B - A) * (min(height[A], height[B]))
        res = max(res, area)
        
        if height[A] < height[B]:
            A += 1
        elif height[A] > height[B]:
            B -= 1
        else:
            A += 1
            B -= 1
    
    return res