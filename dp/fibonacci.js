const fibonacciBottomUp = (n) => {
    const arr = Array(n+1)
    arr[0]=1
    arr[1]=1
    for(let i=2; i<arr.length; i++){
        arr[i]=arr[i-1]+arr[i-2]
    }
    return arr[n]
}

console.log(fibonacci(1))
console.log(fibonacci(4))
console.log(fibonacci(5))