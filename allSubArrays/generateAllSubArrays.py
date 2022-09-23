# [1,2,3] => [1] [2] [3] [1,2] [2,3] [1,2,3]

# O(N^2) algorithm
def allSubArrays(array):
    res = []
    for i in range(len(array)):
        temp = [[array[i]]]
        for j in range(i+1, len(array)):
            newTemp = [temp[-1] + [array[j]]]
            temp += newTemp
        res += temp
    return res


print(allSubArrays([1, 2, 3]))
print(allSubArrays([1, 2, 3, 4]))
print(allSubArrays([1]))
print(allSubArrays([]))
