# Let's first try to solve the problem without
# caring return only the unique combinations.

# i.e. if [2,3] is a solution, then [3,2] is
# also allowed (for now). 

# Since we need all valid combinations, let's
# generate a large number of combinations
# and validify them one by one. This can be done
# using backtracking.

# The philosophy of backtracking is to incrementally
# build candidates to the solutions and abandon canditates
# if they cannot possibly be a valid solution. 

# Note: Each partial sum is actually the sum of a combination
# of the 'canditates' array,

# In the context of the problem, let's incrementally create
# partial sums in a brute-force manner and abandon those
# that cannot be a valid solution. This can avoid us from
# creating an exhaustive number of partial sums (which is
# infinite in this case).

# Since 2 <= candidates[i] <= 40, once the partial sum crosses
# 'target' then it cannot be a valid solution. If it is 'target'
# then the partial sum i.e. combination is a valid solution. 
# Extension of partial sums are not generated in either case.

# A conceptual modelling of this problem using a state-space tree
# can help.

def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    solutions = []
    combination_sum_helper(candidates, target, [], solutions)
    return solutions

def combination_sum_helper(candidates, target, combination, solutions):
    if sum(combination) == target:
        # it is a valid solution.
        solutions.append(combination[:])
        # we append the copy, not the original.
    elif sum(combination) > target:
        # there is no need to extend
        # this branch because it can
        # never reach to a solution.
        return
    else:
        # it is possible that this
        # partial solution can be extended
        # to be arrived at a valid solution.

        # perform extension by adding an
        # element of candidate to this
        # partial solution
        for elem in candidates:
            combination.append(elem)
            combination_sum_helper(candidates, target, combination, solutions)
            combination.pop()

# This code works but we had relaxed our assumption
# of uniqueness hence we get:
# result = [[2, 2, 3], [2, 3, 2], [3, 2, 2], [7]]
# when candidates = [2,3,6,7], target = 7.

# Let's now code it with uniqueness.

# Looking at the state-space tree for candidates = [2,3,6,7]
# and target = 7, we repeat many combinations.

# Eg: we do 6 + 2 but also 2 + 6
# Eg: we do 3 + 2 + 2 but also 2 + 2 + 3

# To avoid this let's create partial sums as follows:
# 2 can add with 2,3,6,7 
# 3 can add with 3,6,7
# 6 can add with 6,7
# 7 can add with 7.

# Since addition is commutative, 6 + 2 will already be
# explored by 2 + 6.
# Similarly, ((3 + 3) + 2) will be explored by ((2 + 3) + 3)

# This will significantly also reduce the calls we have to make.

def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    solutions = []
    combination_sum_helper(candidates, target, [], solutions)
    return solutions

def combination_sum_helper(candidates, target, combination, solutions):
    if sum(combination) == target:
        # it is a valid solution.
        solutions.append(combination[:])
        # we append the copy, not the original.
    elif sum(combination) > target:
        # there is no need to extend
        # this branch because it can
        # never reach to a solution.
        return
    else:
        # it is possible that this
        # partial solution can be extended
        # to be arrived at a valid solution.

        # perform the modified extension 
        # by adding element of candidate to
        # this partial solution
        if not combination:
            start_index = 0
        else:
            start_index = candidates.index(combination[-1])

        for i in range(start_index, len(candidates)):
            combination.append(candidates[i])
            combination_sum_helper(candidates, target, combination, solutions)
            combination.pop()

print(combination_sum([2,3,6,7], 7))
print(combination_sum([2,3,5], 8))
print(combination_sum([2], 1))