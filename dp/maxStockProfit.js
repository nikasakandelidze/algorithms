/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    if(prices.length === 2){
        return Math.max(prices[1] - prices[0],0)
    }
    const dp = Array(prices.length).fill(0)
    let currentLast=prices[prices.length-1]
    for(let i=prices.length-1; i>=0; i--){
        dp[i]=currentLast - prices[i]
        currentLast = Math.max(prices[i], currentLast)
    }
    return Math.max(...dp)
};