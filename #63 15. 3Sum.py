# For 3Sum, if we fix a number, then 
# we are left with the 2Sum problem.

def three_sum(nums: list[int]) -> list[list[int]]:
    solutions = set()
    for i in range(len(nums)):
        # perform 2Sum
        target = 0 - nums[i]
        hashmap = {}
        for j in range(i + 1, len(nums)):
            counterpart = target - nums[j]
            if counterpart not in hashmap:
                hashmap[nums[j]] = j
            else:
                # avoid duplicates: O(1)
                solution = [nums[i], nums[hashmap[counterpart]], nums[j]]
                solution.sort()
                solution = tuple(solution)
                if solution not in solutions:
                    solutions.add(solution)

    return [list(t) for t in solutions]

# This exceeds time on Leetcode. Time complexity: O(n^2)

# Another optimization:
# Sort the array, then fix a number and perform 2Sum II.
# Neetcode's solution

def three_sum(nums: list[int]) -> list[list[int]]:
    solutions = set()

    nums.sort()

    for i in range(len(nums)):
        # perform 2Sum II
        target = 0 - nums[i]

        l = i + 1
        r = len(nums) - 1

        while l < r:
            targ = nums[l] + nums[r]
            if targ < target:
                l += 1
            elif targ > target:
                r -= 1
            elif targ == target:
                # this is a sorted tuple
                solution = (nums[i], nums[l], nums[r])
                if solution not in solutions:
                    solutions.add(solution)
                # consider the next candidates
                l += 1
                r -= 1
    
    return [list(t) for t in solutions]

# Possibly the GOAT solution:
# https://leetcode.com/problems/3sum/solutions/725950/python-5-easy-steps-beats-97-4-annotated

def three_sum(nums: list[int]) -> list[list[int]]:
    results = set()

    pos = []
    neg = []
    zero = []

    for n in nums:
        if 0 < n:
            pos.append(n)
        elif 0 == n:
            zero.append(n)
        elif n < 0:
            neg.append(n)

    POS = set(pos)
    NEG = set(neg)
    
    if zero:
        for p in pos:
            if -p in neg:
                results.add((-p, 0, p))
    
    if len(zero) > 2:
        results.add((0, 0, 0))

    for i in range(len(pos)):
        for j in range(i + 1, len(pos)):
            target = - (pos[i] + pos[j])
            if target in NEG:
                min_p = min(pos[i], pos[j])
                max_p = max(pos[i], pos[j])
                results.add((target, min_p, max_p))

    for i in range(len(neg)):
        for j in range(i + 1, len(neg)):
            target = - (neg[i] + neg[j])
            if target in POS:
                min_n = min(neg[i], neg[j])
                max_n = max(neg[i], neg[j])
                results.add((min_n, max_n, target))

    return [list(t) for t in results]



nums = [-1,0,1,2,-1,-4]
print(three_sum(nums))