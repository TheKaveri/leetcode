# We can do this problem iteratively.

# Idea:
# For the set A = {1,2,3}
# Let P(A) be it's power set that we
# have to generate. For now, P(A) is
# empty.

# 1. Add {} i.e. the empty set to P(A).
# 2. Now pick '1' from A and union it
# with each element for P(A) and add it
# back to P(A).
# 3. Keep repeating step 2. for all 
# subsequent elements of A. 

# Then, P(A) will be the power set of A.

def subsets(nums: list[int]) -> list[list[int]]:
    power_set = [[]]
    # power_set contains the empty set for now

    for num in nums:
        for i in range(len(power_set)):
            # '+' works as a
            # union operator
            power_set.append(power_set[i] + [num])

    return power_set

# Note: Writing 'for set in power_set'
# as the second loop gives generates an
# infinite loop for the above code.

# More concise code:
def subsets(nums: list[int]) -> list[list[int]]:
    power_set = [[]]

    for num in nums:
        power_set += [set + [num] for set in power_set]
    return power_set

# If n is the number of elems in 'nums' then
# 2^n is the number of sets in 'power_set'.
# Since we add an element to 'power_set' in
# each iteration but do an O(n) '+' operation,
# the code takes: O(n * 2^n) time and O(2^n) extra space.

# Another implementation:
# https://www.youtube.com/watch?v=DKCbsiDBN6c
# https://www.youtube.com/watch?v=REOH22Xwdkk

# Backtracking is a way to generate all possible 'solutions'.
# In the context of this problem, a 'solution' is any valid
# subset. We have to generate all possible 'solutions' i.e.
# create the power set.

# Drawing the state-space tree for this problem can help.

def subsets(nums: list[int]) -> list[list[int]]:
    power_set = []
    subset = []

    backtrack(nums, 0, subset, power_set)
    return power_set

def backtrack(set, index, subset, accumulator):
    if index >= len(set):
        accumulator.append(subset[:])
        return
    
    subset.append(set[index])
    backtrack(set, index + 1, subset, accumulator)

    subset.pop()
    backtrack(set, index + 1, subset, accumulator)