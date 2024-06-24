# I tried but I couldn't solve it. So
# I watched these solutions:
# https://www.youtube.com/watch?v=Hi5obC_CwIU
# https://www.youtube.com/watch?v=7ABFKPK2hD4

class Node:
    def __init__(self, key, value) -> None:
        self.key, self.value = key, value
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left = Node(-1, -1)
        self.right = Node(-1, -1)

        self.left.next = self.right
        self.right.prev = self.left

    # removes node from list
    def remove(self, node):
        p = node.prev
        n = node.next

        p.next = n
        n.prev = p

    # inserts at right
    def insert(self,node):
        p = self.right.prev
        n = self.right

        p.next = node
        n.prev = node

        node.next = n
        node.prev = p

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            # return the value but
            # update node position
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value

    def put(self, key: int, value: int) -> None:
        # even if key exists we have to
        # update it's node position after
        # updating the associated value

        # so it's better to abstract away
        # and write a generic code

        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            # remove LRU
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]