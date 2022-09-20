def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def optimizedFibonacciTopDown(n):
    memo = [None for _ in range(n + 1)]

    def helper(m):
        if m == 0 or m == 1:
            return m
        if memo[m]:
            return memo[m]
        result = helper(m - 1) + helper(m - 2)
        memo[m] = result
        return result

    return helper(n)


def optimizedFibonacciBottomUp(n):
    numbers = [-1 for _ in range(n + 1)]
    numbers[0] = 0
    numbers[1] = 1
    for i in range(2, len(numbers)):
        numbers[i] = numbers[i - 1] + numbers[i - 2]
    return numbers[-1]


result2 = optimizedFibonacciTopDown(50)
print('Fibonacci top down: ' + str(result2))
result3 = optimizedFibonacciBottomUp(50)
print('Fibonacci bottom up: ' + str(result3))
result1 = fibonacci(50)
print('Regular fibonacci: ' + str(result1))
