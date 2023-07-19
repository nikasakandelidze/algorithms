class Node:
    def __init__(self, key, val, prev = None, nxt = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = nxt

class LRUCache:
    #   Dictionary + Double LinkedList
    #       O(1) Put and Get with Dictionary
    #       Side effects management and restructuring is done with Linked List
    def __init__(self, capacity: int):
        self.head = None
        self.tail = None
        self.data = {} # Data structure {key: Node(val, prev, nxt)}
        self.capacity = capacity

    def look(self, label):
        print(label)
        temp = self.head
        while temp:
            print(temp.val, end='->')
            temp = temp.next
        print('')

    def get(self, key: int) -> int:
        if key in self.data:
            node = self.data[key]
            if node is self.head:
                return node.val
            elif node is self.tail:
                tail_prev = self.tail.prev
                tail_prev.next = None
                node.prev = None
                self.tail = tail_prev
                node.next = self.head
                self.head.prev = node
                self.head = node
            else:
                node_prev = node.prev
                node_next = node.next
                node_prev.next = node_next
                node_next.prev = node_prev
                node.prev = None
                node.next = self.head
                self.head.prev = node
                self.head = node
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            node = self.data[key]
            # if node is head and tail
            if node is self.head and node is self.tail:
                node.val = value
            # if node is head
            elif node is self.head:
                node.val = value
            # if node is tail
            elif node is self.tail:
                tail_prev = node.prev
                tail_prev.next = None
                node.prev = None
                self.tail = tail_prev
                node.next = self.head
                self.head.prev = node
                self.head = node
                node.val = value
            else:
                node_prev = node.prev
                node_next = node.next
                node_prev.next = node_next
                node_next.prev = node_prev
                node.prev = None
                node.next = self.head
                self.head.prev = node
                self.head = node
                node.val = value
        else:
            new_node = Node(key, value, None, self.head)
            if self.head:
                self.head.prev=new_node
            if not self.tail:
                self.tail = new_node
            self.head = new_node
            self.data[key]=new_node
            if len(self.data) > self.capacity:
                tail_prev = self.tail.prev
                self.tail.prev = None
                tail_prev.next=None
                del self.data[self.tail.key]
                self.tail = tail_prev
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
