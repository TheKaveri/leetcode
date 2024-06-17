import heapq

# Known: 1 <= k <= points.length

# We have a bunch of coordinates and we
# need to give back the k closest ones to
# the origin.

# Idea:
# Use a priority queue where the priority
# is be the euclidean distance of the point
# and the value/element the point itself.

# Assume we have N points, then include all
# of them in a priority queue in the previously
# mentioned manner. Now, to get the 'k' closest
# points, we pop from the priority queue the 'N-k'
# farthest points.

# We need to implement this by using a max-priority
# queue.

def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
    priority_queue = [0] * len(points)

    for i in range(len(points)):
        # no need to really take math.sqrt
        sq_distance = points[i][0] ** 2 + points[i][1] ** 2
        priority_queue[i] = (-sq_distance, points[i])

    heapq.heapify(priority_queue)

    while len(priority_queue) > k:
        heapq.heappop(priority_queue)
    
    k_closest_pts = [0] * len(priority_queue) # i.e. [0] * k

    for i in range(len(priority_queue)):
        k_closest_pts[i] = priority_queue[i][1]
    
    return k_closest_pts

# Time complexity analysis (worst case)
# where n is the size of input:
# T(n) = O(n) + (n-k) * log(n) = n * log(n)

# Here's an implementation that uses min-heaps:
# https://www.youtube.com/watch?v=rI2EBUEMfTk

def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
    priority_queue = []
    for x, y in points:
        # no need to really take math.sqrt
        sq_distance = x ** 2 + y ** 2
        priority_queue.append([sq_distance, x, y])

    heapq.heapify(priority_queue)

    k_closest_pts = []
    while k:
        [_, x, y] = heapq.heappop(priority_queue)
        k_closest_pts.append([x, y])
        k -= 1
    
    return k_closest_pts

# Time compleixty (worst case) is k * log(n)

print(k_closest([[3,3],[5,-1],[-2,4]], 2))