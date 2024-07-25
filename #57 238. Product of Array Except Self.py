# The simplest case is an array of length 2
# as 2 <= nums.length 

# Eg: [1, 2] -> [2, 1]
# Here, we just swap the elements.

# [1, 2, 3] -> [2x3, 1x3, 1x2]
# [1, 2, 3, 4] -> [2x3x4, 1x3x4, 1x2x4, 1x2x3]

def product_except_self(nums: list[int]) -> list[int]:
    products = []
    products.append(nums[1])
    products.append(nums[0])

    for i in range(2, len(nums)):
        last_product = products[-1]
        prev = nums[i - 1]
        products.append(last_product * prev)

        curr = nums[i]
        for j in range(0, len(products) - 1):
            products[j] *= curr
    
    return products

# This approach exceeds time limit. It's not at all efficient.

# I just learned about prefix/postfix sums. Will try to
# use that technique here.

# If nums is [1, 2, 3, 4]
# prefix products are [1, 1x2, 1x2x3, 1x2x3x4]
# postfix products are [1x2x3x4, 2x3x4, 3x4, 4]

# We need [2x3x4, 1x3x4, 1x2x4, 1x2x3]
# Got it!

def product_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    prefix = [1] * n
    postfix = [1] * n
    result = [1] * n
    
    # O(n)
    for i in range(n):
        if i == 0:
            prefix[i] = nums[i]
        else:
            prefix[i] = nums[i] * prefix[i - 1]
    
    # O(n)
    for i in range(n - 1, -1, -1):
        if i == n - 1:
            postfix[i] = nums[i]
        else:
            postfix[i] = nums[i] * postfix[i + 1]

    # O(n)
    for i in range(n):
        if i == 0:
            result[i] = postfix[i + 1]
        elif i == n - 1:
            result[i] = prefix[i - 1]
        else:
            result[i] = prefix[i - 1] * postfix[i + 1]

    return result

# Time is O(n) and extra space is O(n)

# Let's try to acheive O(1) extra space.
# The task is to not create any extra arrays
# other than the one we will be returning.

# Taking a close look at how we construct
# the result from prefix and postfix product
# arrays we see that result is:

# [{}.(2x3x4) , {1}.(3x4), {1x2}.(4), {1x2x3}.()]

# {} -> depicts the numbers from prefix product array
# () -> depicts the numbers from postfix product array

def product_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    result = [1] * n

    prod = 1
    for i in range(1, n):
        prod *= nums[i - 1]
        result[i] *= prod
    
    prod = 1
    for i in range(n - 2, -1, -1):
        prod *= nums[i + 1]
        result[i] *= prod

    return result

nums = [1,2,3,4]
print(product_except_self(nums))