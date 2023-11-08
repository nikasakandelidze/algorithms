/*
     given an amount N and a set of denominations of coins C={C1,C2,C3...} find the minimum number of coins that you need to make up that amount

     coins = [25, 10, 5, 1] amount = 99

     coins = [25, 15, 13, 1] amount = 28  => [25, 1,1,1,] result = 3 which is not correct, the correct result is: [15, 13] where result=2

     Here the problem might be to actually have infinite or finite number of coins
    The greedy algorithm only works here if we for sure know that all larger denominations are multiples of smaller ones
*/
const coinChangeWithMultipleCondition = (coins, amount) => {
    let result = 0
    coins.sort((a,b)=>b-a)
    for(let i=0; i<coins.length; i++){
        if(amount===0){
            return result
        }
        const current = coins[i]
        const order = Math.floor(amount / current)
        result += order
        amount -= order * current
    }
    return result
}

console.log(coinChangeWithMultipleCondition([1, 5, 10, 100], 120))

// DP
// [1,4,21,99,100] 120
const coinChangeWithoutMultipleCondition = (coins, amount) => {
    const amounts = Array(amount+1).fill(Infinity)
    amounts[0] = 0
    for(let i=1; i<amounts.length; i++){
        for(let j=0; j<coins.length; j++){
            if(i >= coins[j]){
                amounts[i] = Math.min(amounts[i], amounts[i-coins[j]]+1)
            }
        }
    }
    return amounts[amounts.length-1]
}


console.log(coinChangeWithoutMultipleCondition([1,4,21,99,100], 120))
console.log(coinChangeWithoutMultipleCondition([2,5,12,15,20], 27))