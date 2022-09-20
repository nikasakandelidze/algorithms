# We must take either full item or not take it at all
# Usually dynamic programming bottom up solutions incorporate some kind of array or grid. Since main idea in bottom up is to solve small problems first and then use them to solve larger problems and in arrays this translates to finding solutions for lower indexes first and only then going to big ones.

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


# elements=[(2kg, 3$) (3kg 4$) (5kg 6$)] maxWeight=8kg
# Dynamic programming, bottom up approach
def optimizedZeroOneKnapSack(elements, maxWeight):
    # (0,0) = (0 value, 0 weight)
    # Two dimensions of grid are: weights(0...maxWeight) and elements(0, 1, 1&2, 1,.....1&2&..len(elements)-1)
    dp = [[0 for _ in range(len(elements)+1)] for _ in range(maxWeight+1)]
    for weight in range(1, len(dp)):
        elementsToConsider = dp[weight]
        for elementIdx in range(1, len(elementsToConsider)):
            element = elements[elementIdx-1]
            if element.weight <= weight:
                # If current element's weight fits into the current weight range that we are looking at
                weightDiff = weight - element.weight
                # choose max between: currentElement + element that also fits with it in the current weight | previous solution without current element and with the same weight.
                dp[weight][elementIdx] = max(element.val+dp[weightDiff][elementIdx-1], dp[weight][elementIdx-1])
            else:
                # If the current element's weight is more than the weight we are looking at choose as current solution previous element's solution for the same weight.
                # Since it means that current element is itself larger than the weight so we shouldn't even consider itself alone, let alone it's combination with some other values.
                dp[weight][elementIdx] = dp[weight][elementIdx-1]
    return dp[-1][-1]


item1 = Item(20, 20, 'gold')
item2 = Item(60, 30, 'silver')
item3 = Item(20, 10, 'bronze')
item4 = Item(20, 40, 'wazap')
item5 = Item(20, 10, 'bronze2')
items = [item1, item2, item3, item4, item5]
result1=zeroOneKnapSack(items, 50)
result2=optimizedZeroOneKnapSack(items, 50)
print(result1)
print(result2)
