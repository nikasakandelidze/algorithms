class MinStack:
    def __init__(self):
        self.elems = []
        self.mins = []

    def push(self, val: int) -> None:
        self.elems.append(val)
        if not self.mins:
            self.mins.append(val)
        else:
            self.mins.append(min(self.mins[-1], val))

    def pop(self) -> None:
        self.elems.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.elems[-1]

    def getMin(self) -> int:
        return self.mins[-1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(3)
assert obj.top() == 3
assert obj.getMin() == 3
obj.push(4)
assert obj.top() == 4
assert obj.getMin() == 3
obj.push(1)
assert obj.top() == 1
assert obj.getMin() == 1