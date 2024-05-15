# I think diagrammatizing the problem would offer
# much insight into the logic of operations like
# deletion, insertion etc. So I will not be going
# through it step by step here.

# However, I want to add some notes on deleteAtIndex

# To delete a an arbitrary node, we have to manipulate
# it's 'previous' and 'next' nodes. However the catch is that
# head doesn't have a 'previous' node and tail doesn't have
# a 'next' node. 

# I first coded this deleteAtIndex logic for a node with valid
# 'previous' and 'next' nodes:

# 1. prev_of_curr = curr.prev
# 2. next_of_curr = curr.next
# 3. prev_of_curr.next = next_of_curr
# 4. next_of_curr.prev = prev_of_curr

# And then, I tweaked it to handle for scenarios where head and
# tail are the nodes being deleted. 

class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        i = 0
        curr = self.head

        while curr:
            if i == index:
                return curr.val
            else:
                i += 1
                curr = curr.next
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        if not self.head and not self.tail:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        self.length += 1
            

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        if not self.head and not self.tail:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        else:
            i = 0
            curr = self.head

            while curr:
                if i == index:
                    # add to any middle position
                    new_node = ListNode(val)
                    prev_of_curr = curr.prev

                    prev_of_curr.next = new_node
                    new_node.next = curr

                    curr.prev = new_node
                    new_node.prev = prev_of_curr

                    self.length += 1
                    break
                else:
                    i += 1
                    curr = curr.next
        

    def deleteAtIndex(self, index: int) -> None:
        # Generic case is deleting any middle node -> can 
        i = 0
        curr = self.head

        while curr:
            if i == index:
                # delete curr
                prev_of_curr = curr.prev
                next_of_curr = curr.next

                if prev_of_curr:
                    prev_of_curr.next = next_of_curr
                else: # curr is self.head
                    self.head = next_of_curr

                if next_of_curr:
                    next_of_curr.prev = prev_of_curr
                else: # curr is self.tail
                    self.tail = prev_of_curr
                    
                self.length -= 1
                break
            else:
                i += 1
                curr = curr.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)