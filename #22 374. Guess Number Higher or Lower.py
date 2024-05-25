# This question is a simple variant of the original
# binary search algorithm.

def guess_number(self, n: int) -> int:
        start, end = 1, n

        while start <= end:
            num = (start + end) // 2

            if guess(num) == -1:
                  # pick < num
                  end = num - 1
            elif guess(num) == 1:
                  # num < pick
                  start = num + 1
            else:
                # guess(num) == 0
                return num

# A simulation of the API. 
def guess(num: int) -> int:
    pick = 10
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:
        return 0