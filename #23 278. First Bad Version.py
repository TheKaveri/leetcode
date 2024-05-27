# The easiest approach is to call the 'isBadVersion'
# API starting from 1,2,3 and so on until we reach
# the first version that makes 'isBadVersion' true.

# It's given that 1 <= bad <= n <= 2^31 - 1
# Also, the latest version is bad i.e. isBadVersion(n)
# gives true.

def first_bad_version(n: int) -> int:
    for version in range(1, n + 1):
        if is_bad_version(version):
            return version

# A simulation of the API. 
def is_bad_version(version: int) -> bool:
    return version == 7

# This takes O(n) time and O(1) extra space.

# Let's try doing better using the binary search
# technique.

# If mid happens to be a good version, then the first
# bad version is somewhere in the future.

# If mid is a bad version, check if it is the first bad
# version by asking whether the predecessor of mid is a
# bad version or not. If the predecessor is a bad version
# then the first bad version is in the past, otherwise
# the first bad version is mid.

# Note that for version 1, there is no predecessor so
# if version 1 is bad, then the first bad version is 1.

def first_bad_version(n: int) -> int:
    if n == 1:
        return n
    
    start, end = 1, n
    while start <= end:
        mid = (start + end) // 2

        if is_bad_version(mid):
            previous = mid - 1
            if is_bad_version(previous):
                # mid is not the first bad
                # version
                end = mid - 1
            else:
                # mid is the first bad
                # version
                return mid
        else:
            # mid is not a bad version so
            # the first bad version must 
            # be in the future.
            start = mid + 1

# This takes O(log(n)) time and O(1) extra space.