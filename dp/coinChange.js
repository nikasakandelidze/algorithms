var coinChange = function(coins, amount) {
    const dp = Array(amount+1).fill(Infinity)
    dp[0] = 0
    // coins.sort() //is this mandatory ?
    for(const coin of coins){
        for(let i=1; i<dp.length; i++){
            if(coin <= i){
                dp[i]=Math.min(dp[i], 1+dp[i-coin])
            }
        }
    }
    return dp[amount] === Infinity ? -1 : dp[amount]
    
};