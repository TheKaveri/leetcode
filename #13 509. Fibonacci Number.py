# This is a really basic question so I will
# straight away code it up. 

# Will come back to it later to impelement a solution
# using memoization / dynamic-programming.


# Recursive implementation:
def fib(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

# Takes O(2^n) time and O(n) space
# Complexity analysis:
# https://stackoverflow.com/questions/28756045/what-is-the-space-complexity-of-a-recursive-fibonacci-algorithm
# https://www.youtube.com/watch?v=ncpTxqK35PI

# Iterative implementation:

def fib(n: int) -> int:
    if n <= 1:
        return n
    else:
        fib_a = 0
        fib_b = 1
        term = 2
        while term <= n:
            fib_c = fib_b + fib_a
            # Careful here:
            fib_a = fib_b
            fib_b = fib_c
            term += 1
        
        return fib_c


print(fib(4))