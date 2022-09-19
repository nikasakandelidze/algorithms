# We can also take any fractions of any items

# Pattern: if 2 parameters are present for each element/item in collection
# Think about how some kind of combination of these two properties can be used to calculate something meaningful.

class Item:
    def __init__(self, val, weight, label):
        self.label=label
        self.val = val
        self.weight = weight

# This is a greedy algorithm in a sense that it's a sequence of decisions
# each simply making a decision based on the local optimums. and appearently it ends up as a global optimum
# This is kind of a greedy algorithm that doesn't need a backtrack mechanism an is a direct solution


def fractionalKnapSack(items, maxWeight):
    valsPerUnitOfWeight = list(map(lambda x: (x.val / x.weight, x), items))
    valsPerUnitOfWeight.sort(key=lambda x: x[0], reverse=True)
    result=[]
    sumOfValues=0
    leftWeight=maxWeight
    for valPerUnit, item in valsPerUnitOfWeight:
        kilos=item.weight
        if kilos < leftWeight:
            sumOfValues += valPerUnit * kilos
            result.append((kilos, item.label))
            leftWeight -= kilos
        else:
            sumOfValues += valPerUnit * leftWeight
            result.append((leftWeight, item.label))
            break
    return (result, sumOfValues)


gold=Item(50,20,'Gold')
silver=Item(50, 50, 'Silver')
bronze=Item(50, 100, 'Bronze')
result=fractionalKnapSack([silver,gold,bronze], 50)
print(result)