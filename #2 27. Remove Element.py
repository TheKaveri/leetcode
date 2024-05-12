# Idea:
# Go through the list one by one, if we hit val, then swap it
# with the first element that is not val when working backward from 
# end of list i.e. in reversed manner.

# Eg: {1,2,6,5,2,2}, val = 2
# Then the first element that is not val when working backward from end of list is 5.
# Eg: {0,1,2,2,3,0,4,2}, val = 2
# Then the first element that is not val when working backward from end of list is 4.
# Lets call such elements the F-element.
# Note that if there are any elements in front of F-element, they are always vals.
# This is true by the definition of F-element.

# Because of the swaps, elements that are val will start accumulating toward the 
# end of the list. We stop once all vals have accumulated at the end. I.e. when
# F-element is behind all the vals.

# Cases where we fail to find F-element are when the list is a collection of vals.
# In this case, return 0 as there are 0 elements other than val.

def remove_element(nums: list[int], val: int) -> int:
    for i in range(len(nums)):
        if nums[i] == val:
            f_element_index = get_f_element_index(nums, val)
            if f_element_index == -1:
                # no element other than val exists in list
                return 0
            
            if f_element_index > i:
                # swap
                nums[i], nums[f_element_index] = nums[f_element_index], nums[i]
            else:
                # f_element_index == i is impossible as nums[f_element_index] != nums[i]
                # so else happens when when f_element_index < i
                # so f_element_index is the position after which all elements are vals
                return f_element_index + 1
                
                
def get_f_element_index(nums: list[int], val: int) -> int:
    """Find the F-element index, or return -1 if failed"""
    for j in range(len(nums) - 1, -1, -1):
        if nums[j] != val:
            return j
    return -1

# This solution is great. It takes O(n) time and no additional space.
# However, the logic and handling of the edge cases could be much simpler.

# Here's a much simpler solution:
# https://youtu.be/Pcd1ii9P9ZI?si=8ictrNOAgPQcBZXu

def remove_element(nums: list[int], val: int) -> int:
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k
