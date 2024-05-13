# The problem is not much different from impelementing a
# regular stack. The only catch is keeping track of the
# minimum element. I initially did this by using a single
# integer variable named 'self.min'. But this approach is
# incorrect, as we can't update 'self.min' if the mimimum
# element happens to be removed from the stack.

# Eg: stack -> {7, 1, 10, 4, 3, -2}
# Currently, self.min = -2
# After popping, stack -> {7, 1, 10, 4, 3}
# But there is no way to update self.min unless we somehow 
# store the values that were the mimimum element at some 
# point in time. This is preferrable to scanning the stack
# to find the minimum element since we need O(1) for all
# methods.

# Eg: stack -> {7, 1, 10, 1, 4, 3, -2}
# Then self.mins = [math.inf, 7, 1, 1, -2]

import math
class MinStack:

    def __init__(self):
        self.arr = []
        self.mins = [math.inf]

    def push(self, val: int) -> None:
        if val <= self.mins[-1]:
            self.mins.append(val)
        self.arr.append(val)

    def pop(self) -> None:
        val = self.arr.pop()
        if val == self.mins[-1]:
            self.mins.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.mins[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()