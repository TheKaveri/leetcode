# The naive way is to go through each
# element one by one and find if there
# is another element such that the current 
# element and the other one add up to 'target'.

# While looking for the other element, we can
# search in the array subsection ahead of the
# current element.

# Reason:
# Say nums[0] has no match in the array, then
# elements nums[i] for i starting from 1 and
# onwards can never match with nums[0].

# Similarly, if nums[1] has no match, then
# elements nums[i] for i starting from 2 and
# onwards can never match with nums[1].
# Combining previous observation, they don't
# match with nums[0] as well as nums[1].

# So there is no need to look 'behind' as long
# as we are looking for a solution.

# Note: We are guaranteed to have a solution.        
def two_sum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# The time complexity of this is O(n^2)

# The problem is with the search of nums[j]
# that takes O(n). However, hashmaps allow
# O(1) searching. Let's try to solve the problem
# using hashmaps.

# If A + B = target, then B is A's counterpart and
# vice-versa.

# We initialize an empty hashmap. Then we iterate
# through nums. If nums[i]'s counterpart doesn't
# exist in the hashmap, we store an entry to it
# as follows: 
# key is 'nums[i]' and value is 'i'

# If the counterpart does exist, then we have
# solved the problem. We just return the value
# associated with the counterpart along with 
# the index of the current element.

def two_sum(nums: list[int], target: int) -> list[int]:
    hashmap = {}
    for i in range(len(nums)):
        counterpart = target - nums[i]
        if counterpart not in hashmap:
            hashmap[nums[i]] = i
        else:
            return [hashmap[counterpart], i]

# The time complexity of this is O(n) as the
# search for the counterpart takes O(1) time.

# The extra space taken is O(n)