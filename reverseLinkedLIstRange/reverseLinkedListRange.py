class LinkedList:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def printLinkedList(head):
    while head:
        print(str(head.val) + '->', end='')
        head = head.next
    print('None', '')

# 1 -> 2 -> 3 -> 4 -> 5  (1, 3)


def reverseLinkedListRange(head, start, end):
    idx = 0
    prev = None
    temp = head
    newHeadPrevNode, newTailNextNode = None, None
    newTail, newHead = None, None
    while temp:
        if start <= idx <= end:
            if idx == start:
                newTail = temp
            elif idx == end:
                newHead = temp
            nxt = temp.next
            if idx != start:
                temp.next = prev
            prev = temp
            temp = nxt
            idx += 1
        else:
            if start > 0 and idx == start - 1:
                newHeadPrevNode = temp
            if idx == end + 1:
                newTailNextNode = temp
            idx += 1
            prev = temp
            temp = temp.next
    if newHeadPrevNode:
        newHeadPrevNode.next = newHead
    newTail.next = newTailNextNode
    return newHead if not newHeadPrevNode else head


five = LinkedList(5)
four = LinkedList(4, five)
three = LinkedList(3, four)
two = LinkedList(2, three)
one = LinkedList(1, two)

printLinkedList(one)
print('Reverse range (0,4)')
result = reverseLinkedListRange(one, 0, 4)
print('Result: ',end="")
printLinkedList(result)

print()

five = LinkedList(5)
four = LinkedList(4, five)
three = LinkedList(3, four)
two = LinkedList(2, three)
one = LinkedList(1, two)

printLinkedList(one)
print('Reverse range (1,3)')
result = reverseLinkedListRange(one, 1, 3)
print('Result: ',end="")
printLinkedList(result)

print()


five = LinkedList(5)
four = LinkedList(4, five)
three = LinkedList(3, four)
two = LinkedList(2, three)
one = LinkedList(1, two)

printLinkedList(one)
print('Reverse range (0,1)')
result = reverseLinkedListRange(one, 0, 1)
print('Result: ',end="")
printLinkedList(result)


print()

five = LinkedList(5)
four = LinkedList(4, five)
three = LinkedList(3, four)
two = LinkedList(2, three)
one = LinkedList(1, two)

printLinkedList(one)
print('Reverse range (3,4)')
result = reverseLinkedListRange(one, 3, 4)
print('Result: ',end="")
printLinkedList(result)