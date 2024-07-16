# Given: 1 <= n 

# Iterative solution:
def hamming_weight(n: int) -> int:
    count = 0
    while n > 0:
        if n & 1 == 1:
            count += 1
        n = n >> 1
    return count