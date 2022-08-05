def powerSet(data):
    if not data:
        return [[]]
    current = data[0]
    res = powerSet(data[1:])
    extended_res = [x + [current] for x in res]
    return extended_res + res


result1 = powerSet([1,2,3])
print(result1)

result2 = powerSet([1])
print(result2)

result3 = powerSet([])
print(result3)
