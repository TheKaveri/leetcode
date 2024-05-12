# This question can be done easily by calling the list.extend(iterable) method on ans twice.
# However, this performance overhead since we have to dynamically resize ans. This is because
# dynamic resizing takes more time (i.e. allocate memory and copy elements, then deallocate)
# and more space (due to overallocation of memory) compared to preallocated memory.

def get_concatenation(nums: list[int]) -> list[int]:
    n = len(nums)
    ans = [0] * 2 * n

    for i in range(n):
        ans[i], ans[i + n] = nums[i], nums[i]
    
    return ans

# The below solutions use dynamic resizing and are hence comparatively less desirable for 
# large inputs. The code is sweet though.

def get_concatenation(nums: list[int]) -> list[int]:
    ans = []
    ans.extend(nums)
    ans.extend(nums)
    return ans

def get_concatenation(nums: list[int]) -> list[int]:
    return nums + nums