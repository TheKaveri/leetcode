# The simplest way to perform a search on a
# 2D matrix is to look at every element one by
# one. However, this takes O(m * n) time.

# We can certainly do better since the matrix is
# well ordered. 

# The second approach is to look at each row and
# see if:
# row[0] <= target <= row[-1]
# i.e. if the target can be in the range of the row's
# first and last element then it could potentially exist in
# that row. If the condition is true, then we perform binary
# search. Else we try the next row as target cannot exist there.

def search_matrix(matrix: list[list[int]], target: int) -> bool:
    for row in matrix:
        if row[0] <= target <= row[-1]:
            return binary_search(row, target)
    return False
def binary_search(nums: list[int], target: int) -> bool:
    start, end = 0, len(nums) - 1

    while start <= end:
        mid = (start + end) // 2

        if nums[mid] < target:
            start = mid + 1
        elif target < nums[mid]:
            end = mid - 1
        else:
            return True
    return False

# This takes O(m * logn) time. O(m) to go through each row
# and O(logn) for the search itself. Extra space is O(1).

# However, we need O(log(m * n)). This is like performing
# binary search on a single array of m * n elements.

# We can convert the matrix into a list and perform
# binary search on that list. This would take O(m + log(m * n)).
# O(m) to create the list and O(log(m * n)) for the search.
# Extra space would be O(m * n).

# The right way is to perform binary search on the matrix directly
# by treating the matrix as a list.

# Since we have two-way indexing for matrices, each element can be
# assigned a position as follows:
# Element at (i,j) is (n * i + j)th element.
# Call it the Kth element.

# Note that i is always in [0, m-1] and j is always in [0, n-1].
# Therefore j is never a multiple of n.

# We know: n * i + j = K

# So, any element at position K will be at index (i, j) where:
# j = K mod(n)
# i = (K - j) / n

# This can let us treat the matrix as a list.
def search_matrix_this(matrix : list[list[int]], target: int) -> bool:
    m = len(matrix) # row count
    n = len(matrix[0]) # col count

    start, end = 0, n * m - 1

    while start <= end:
        mid = (start + end) // 2
        j = mid % n
        i = (mid - j) // n
        # mid  - j will always be a multiple of n.
        # I have used '//' to void floating point.

        if matrix[i][j] < target:
            start = mid + 1
        elif target < matrix[i][j]:
            end = mid - 1
        else:
            return True
    return False

# This takes O(log(m * n)) time and O(1) extra space.

matrix = [[1,1]]
target = 2
print(search_matrix_this(matrix, target))