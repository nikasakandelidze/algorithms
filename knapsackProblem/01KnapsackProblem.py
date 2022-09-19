# We must take either full item or not take it at all


class Item:
    def __init__(self, val, weight, label):
        self.label = label
        self.val = val
        self.weight = weight


# brute force algorithm. Runs in exponential time 2^N. Not so good:)
def zeroOneKnapSack(elements, maxWeight):
    def helper(elements, index, weightLeft):
        if weightLeft == 0:
            return 0
        if index >= len(elements) or weightLeft < 0:
            return -1  # flag for incorrect solution
        res1 = helper(elements, index + 1, weightLeft - elements[index].weight)
        if res1 != -1:
            res1 += elements[index].val
        res2 = helper(elements, index + 1, weightLeft)
        return max(res1, res2)
    return helper(elements, 0, maxWeight)


item1 = Item(20, 20, 'gold')
item2 = Item(60, 30, 'silver')
item3 = Item(20, 10, 'bronze')
item4 = Item(20, 40, 'wazap')
item5 = Item(15, 10, 'bronze2')
items = [item1, item2, item3, item4, item5]
result=zeroOneKnapSack(items, 50)
print(result)
