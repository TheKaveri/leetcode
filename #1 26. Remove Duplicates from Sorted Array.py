def remove_duplicates(nums: list[int]) -> int:
        nums_wihout_duplicates = []
        for elem in nums:
            if elem not in nums_wihout_duplicates:
                nums_wihout_duplicates.apped(elem)
        return len(nums_wihout_duplicates)

# To solve the problem without using an
# additional list, use the original list itself
# as a storage for the unique elements, but use
# the same technique as shown above.

def remove_duplicates(nums: list[int]) -> int:
        length = 0
        for elem in nums:
            if elem not in nums[:length]:
                nums[length] = elem
                length += 1
        return length

# This approach is great, it doesn't use an additional list
# but it's not efficient because of the "not in" check
# which takes O(n) for lists. Also the slicing
# of the list takes O(n) space, which is not good
# for large lists.

# We are given that nums will have at least 1 element,
# so we know the first element is always in the solution.

# We also know the array is sorted, this avoids the
# need to check elem in nums[:length]. We can just
# check the end of the list.

def remove_duplicates(nums: list[int]) -> int:
        length = 1
        for elem in nums[1:]:
            if elem != nums[length - 1]:
                nums[length] = elem
                length += 1
        return length

# or better so (as we avoid generating a list slice):

def remove_duplicates(nums: list[int]) -> int:
        length = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[length - 1]:
                nums[length] = nums[i]
                length += 1
        return length