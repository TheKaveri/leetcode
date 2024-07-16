# Let's try to generate the answer
# bit by bit.

# Since input always has 32-bits and each
# work we do on a bit is O(1), the time
# complexity will be O(32) = O(1)

def reverse_bits(n: int) -> list[int]:
    rev_bits = []
    for _ in range(32):
        rev_bits.append(n & 1)
        n = n >> 1
    return rev_bits

# Now that we've managed to solve using
# lists, lets try to solve using ints.
def reverse_bits(n: int) -> int:
    rev_no = 0
    for _ in range(32):
        # append analogue
        rev_no = rev_no << 1 
        rev_no += n & 1
        n = n >> 1
    return rev_no