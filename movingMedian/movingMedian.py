import heapq


class MaxHeap:
    def __init__(self):
        self.data = []

    def add(self, value):
        heapq.heappush(self.data, -1 * value)

    def peek(self):
        return -1 * self.data[0]

    def pop(self):
        return -1 * heapq.heappop(self.data)

    def __len__(self):
        return len(self.data)


class MinHeap:
    def __init__(self):
        self.data = []

    def add(self, value):
        heapq.heappush(self.data, value)

    def peek(self):
        return self.data[0]

    def pop(self):
        return heapq.heappop(self.data)

    def __len__(self):
        return len(self.data)


class MedianFinder(object):

    def __init__(self):
        self.left = MaxHeap()
        self.right = MinHeap()

    def _moveOneElement(self, fromHeap, toHeap):
        element = fromHeap.pop()
        toHeap.add(element)

    # O(Log(N))
    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if not self.left and not self.right:
            self.left.add(num)
        else:
            added = False
            if len(self.left) > 0:
                left_max = self.left.peek()
                if left_max > num:
                    self.left.add(num)
                    added = True
            if len(self.right) > 0:
                right_min = self.right.peek()
                if right_min < num:
                    self.right.add(num)
                    added = True
            if not added:
                self.left.add(num)
            if len(self.left) - len(self.right) >= 2:
                self._moveOneElement(self.left, self.right)
            elif len(self.right) - len(self.left) >= 2:
                self._moveOneElement(self.right, self.left)

    # O(1)
    def findMedian(self):
        """
        :rtype: float
        """
        if not self.left and not self.right:
            return -1
        if (len(self.left.data) + len(self.right.data)) % 2 == 0:
            return float((self.left.peek() + self.right.peek())) / 2
        else:
            if len(self.left) > len(self.right):
                return self.left.peek()
            else:
                return self.right.peek()

# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
obj.addNum(3)
obj.addNum(11)
result = obj.findMedian()
assert result ==2.5