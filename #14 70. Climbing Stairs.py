# Domain of n: [1,45]

# Instead of climbing a staircase, think about descending
# a staircase. If it takes n steps to reach the top, then
# it takes n steps to reach the bottom. It is given that
# we can climb 1 or 2 steps so we can descend 1 or 2 steps.

# In short, the problem is the same as asking:
# 'How many distinct ways can we descend from to the top to
# the bottom?'

# Given n steps, a person at the top can descend 1 step
# and descend the rest, or they can descend 2 steps and
# descend the rest. 

# So number of distinct ways to descend n steps from top 
# to bottom is number of distinct ways to descend n-1 steps
# added with number of distince ways to descend n-2 steps.

# For one step, there is one distinct way.
# For two steps, there are two distinct ways.

# Note: try drawing a decision tree for n = 4 and then n = 5

# So, f(n) = f(n-1) + f(n-2) and f(1) = 1, f(2) = 2. This is
# behaves quite close to the Fibonnaci sequence.

def count_distinct_descend(n: int) -> int:
    if n <= 2:
        return n
    else:
        return count_distinct_descend(n - 1) + count_distinct_descend(n - 2)
    
# This like the recursive fibonacci function takes O(2^n) time and O(n) space.

# Here's a better implementation:

def count_distinct_descend(n: int) -> int:
    distinct_descends = [-1, 1, 2]
    # We have to construct this list until distinct_descends[n]
    # is a valid entry. So we go until the size of distinct_descends
    # hits n + 1.

    while len(distinct_descends) < n + 1:
        distinct_descends.append(distinct_descends[-1] + distinct_descends[-2])

    return distinct_descends[n] # which is actually distinct_descends[-1]
    
# We can further optimize it by preallocating a some space for the list. Right now
# we are appending to the array, which causes dynamic resizing of distinct_descends.

def count_distinct_descend(n: int) -> int:
    if n <= 2:
        return n
    else:
        distinct_descends = [0] * (n + 1)
        distinct_descends[1] = 1
        distinct_descends[2] = 2

        for i in range(3, n + 1):
            distinct_descends[i] = distinct_descends[i - 1] + distinct_descends[i - 2]

        return distinct_descends[n] # which is actually distinct_descends[-1]
    
def count_distinct_descend(n: int) -> int:
    if n <= 2:
        return n
    else:
        count_descent_a = 1
        count_descent_b = 2
        term = 3
        while term <= n:
            count_descent_c = count_descent_b + count_descent_a
            count_descent_a = count_descent_b
            count_descent_b = count_descent_c
            term += 1

        return count_descent_c