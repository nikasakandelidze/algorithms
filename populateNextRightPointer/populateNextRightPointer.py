from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        queue = []
        queue.append(root)
        while queue:
            nxt = None
            temp_queue = []
            while queue:
                element = queue.pop(0)
                element.next = nxt
                nxt = element
                if element.right: temp_queue.append(element.right)
                if element.left: temp_queue.append(element.left)
            queue += temp_queue
        return root