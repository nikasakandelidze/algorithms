import heapq


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    head = None
    tail = None
    data = []
    for i in range(len(lists)):
        node = lists[i]
        if node is not None:
            heapq.heappush(data, (node.val, i, node))
            lists[i] = lists[i].next
    while data:
        val, idx, node = heapq.heappop(data)
        if tail:
            tail.next = node
        else:
            head = node
        tail = node
        if lists[idx]:
            heapq.heappush(data, (lists[idx].val, idx, lists[idx]))
            lists[idx] = lists[idx].next
    return head


def printLinkedList(node):
    while node is not None:
        print(str(node.val) + '->',end="")
        node = node.next


first = ListNode(1, ListNode(2, ListNode(4, None)))
second = ListNode(1, ListNode(6))
third = ListNode(2, ListNode(2, ListNode(3)))
array = [first, second, third]

result = mergeKLists(array)
printLinkedList(result)
