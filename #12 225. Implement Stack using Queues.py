# Since, Python3 doesn't support queues natively, lists will
# be used to solve the problem. The following list operations
# are the only ones allowed (since we have to simulate queues 
# using lists):

# 1. queue.append(value)
# 2. queue.pop(0)
# 3. queue[0] (for simulating peek)
# 4. if queue / while queue (for is_empty? checks)
# 5. len(queue)

# I'll first use two queues to solve the problem, and then later
# solve the problem with one queue.

# Some approaches with two queues:

# 1. Store the elements in the order they were added but shuffle
# them around when popping.

# Eg: We insert a, b and c in MyStack. Internally:
# input_queue -> {a, b, c}
# shuffle_queue -> {}

# Now, keep popping from the front of the input_queue and adding to end of
# shuffle_queue until we reach a state where:
# input_queue -> {c}
# shuffle_queue -> {a, b}

# Now, pop and return 'c' to maintain the LIFO property of MyStack, and
# reassign the queues by swapping them. This gives us:
# input_queue -> {a, b}
# shuffle_queue -> {c}

# The same logic applies for getting 'b' from MyStack.
# Here's the code for this approach:
class MyStack:

    # O(1)
    def __init__(self):
        # self.input_queue = self.shuffle_queue = [] -> this is wrong
        # as throughout the code, they will refer to the same array
        self.input_queue = []
        self.shuffle_queue = []

    # O(1)
    def push(self, x: int) -> None:
        self.input_queue.append(x)

    # O(n)
    def pop(self) -> int:
        while len(self.input_queue) != 1:
            value = self.input_queue.pop(0)
            self.shuffle_queue.append(value)
        
        value = self.input_queue.pop(0)
        self.input_queue, self.shuffle_queue = self.shuffle_queue, self.input_queue

        # now 'value' is the last element that
        # was removed
        return value

    # O(n)
    def top(self) -> int:
        # First we pop, then we undo the pop
        # and then return the value
        value = self.pop()
        self.input_queue.append(value)
        return value

    def empty(self) -> bool:
        if not self.input_queue:
            return True
        else:
            return False
        
# Let's try the second approach:

# 1. Store the elements in reverse order in which they were added
# so that we can pop or top in O(1)

# Idea:
# retreival_queue's role is to store the elements in reverse order.
# reversal_queue's role is to help us generate the elements in reverse order.

# Each time we wish to insert an element in MyStack, put it
# in reversal_queue. Then pop from front of retreival_queue and
# add at end of reversal_queue until retreival_queue is empty.

# Finally, swap the queues so that they restore their designated roles.

class MyStack:

    # O(1)
    def __init__(self):
        # self.retreival_queue = self.reversal_queue = [] -> this is wrong
        # as throughout the code, they will refer to the same array
        self.retreival_queue = []
        self.reversal_queue = []

    # O(n)
    def push(self, x: int) -> None:
        self.reversal_queue.append(x)

        while self.retreival_queue:
            value = self.retreival_queue.pop(0)
            self.reversal_queue.append(value)

        self.retreival_queue, self.reversal_queue = self.reversal_queue, self.retreival_queue

    # O(1)
    def pop(self) -> int:
        return self.retreival_queue.pop(0)

    # O(1)
    def top(self) -> int:
        return self.retreival_queue[0]

    # O(1)
    def empty(self) -> bool:
        if not self.retreival_queue:
            return True
        else:
            return False
        
# This is a much better solution since we have only one method with O(n) time compared
# to two methods in the previous algorithm.

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

my_stack = MyStack()
my_stack.push(1)
my_stack.push(2)
print(my_stack.top())
print(my_stack.pop())
print(my_stack.empty())

# Now implementing MyStack with only one queue:

# We can apply the same logic we used with retreival_queue
# and reversal_queue.

class MyStack:

    # O(1)
    def __init__(self):
        self.queue = []

    # O(n)
    def push(self, x: int) -> None:
        original_queue_size = len(self.queue)
        self.queue.append(x)

        for _ in range(original_queue_size):
            # this basically shifts all elements in the back
            # except for the element 'x' that was inserted.
            value = self.queue.pop(0)
            self.queue.append(value)

    # O(1)
    def pop(self) -> int:
        return self.queue.pop(0)

    # O(1)
    def top(self) -> int:
        return self.queue[0]

    # O(1)
    def empty(self) -> bool:
        if not self.queue:
            return True
        else:
            return False