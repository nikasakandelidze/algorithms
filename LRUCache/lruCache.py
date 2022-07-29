class Node:
    def __init__(self, key, value, next_node=None, prev_node=None):
        self.key = key
        self.val = value
        self.nxt = next_node
        self.prev = prev_node


class LRUCache:
    def __init__(self, capacity: int):
        self.data = {}
        self.head = None
        self.tail = None
        self.capacity = capacity
        self.logLen = 0
    
    def get(self, key: int) -> int:
        if key in self.data:
            node = self.data[key]
            if node is self.head:
                return node.val
            else:
                node.prev.nxt = node.nxt
                if node.nxt is not None:
                    node.nxt.prev = node.prev
                else:
                    self.tail = node.prev
                node.nxt = self.head
                node.prev = None
                self.head.prev = node
                self.head = node
                return node.val
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.data:
            node = self.data[key]
            node.val = value
            if node is not self.head:
                node.prev.nxt = node.nxt
                if node.nxt is not None:
                    node.nxt.prev = node.prev
                else:
                    self.tail = node.prev
                node.nxt = self.head
                self.head.prev = node
                self.head = node
        else:
            self.logLen += 1
            node = Node(key, value)
            self.data[key] = node
            if not self.head:
                self.head = node
                self.tail = node
            else:
                self.head.prev = node
                node.nxt = self.head
                self.head = node
            if self.logLen > self.capacity:
                tail_node = self.tail
                new_tail = tail_node.prev
                new_tail.nxt = None
                del self.data[tail_node.key]
                self.tail = new_tail
                self.logLen -= 1


# Check mechanism
cache = LRUCache(2)
print('put (1,2)')
cache.put(1,2)
print('cache.get(1) == 2 is', cache.get(1) == 2)
print('put (1,3)')
cache.put(1,3)
print('cache.get(1) == 3 is', cache.get(1) == 3)
print('put (2,2)')
cache.put(2,2)
print('cache.get(2) == 2 is', cache.get(2) == 2)
print('put (4,2)')
cache.put(4,2)
print('cache.get(4) == 2 is', cache.get(4) == 2)
print('cache.get(1) should be -1', cache.get(1) == -1)