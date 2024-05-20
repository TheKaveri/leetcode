# Idea:
# Let's convert 'nums' into a set, and then back to
# a list. Then let's compare if the new list and 'nums'
# have same number of elements.

def contains_duplicate(nums: list[int]) -> bool:
    return len(nums) != len(set(nums))

# Idea:
# Create a dictionary that keeps track of how many times
# a value appears 'nums'. If all the values appear only
# once, then we have no duplicates, otherwise we do.

def contains_duplicate(nums: list[int]) -> bool:
    element_frequency = {}

    for element in nums:
        if element not in element_frequency: # or element_frequency.keys()
            element_frequency[element] = 1
        else:
            element_frequency[element] += 1

    for _, frequency in element_frequency.items():
        if frequency != 1:
            return True
    return False

# This solution takes a worst-case O(n) time and O(n) extra space.
# But it could be much simpler in terms of logic. We actually don't need
# to keep track of the frequency of each and every element.

# Idea:
# Create a set, and keep adding the elements if it is not in the set. 
# If the element is in the set, then we have a duplicate.

# Note: set operations take O(1) time for lookup/deletion/insertion.

def contains_duplicate(nums: list[int]) -> bool:
    nums_set = set()

    for element in nums:
        if element not in nums_set:
            nums_set.add(element)
        else:
            # There is a duplicate
            return True
    
    # All elements appear only once since 
    # 'else' hasn't satisfied for any element.
    return False

# Note: Duplicates that exist in a sorted array will always be adjacent. 