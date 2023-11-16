/**
 * @param {number[]} prices
 * @return {number}
 */

// [7,1,5,3,6,4]
// [1,2,3,4,5]
var maxProfit = function(prices) {
    const cache = {}
    const helper = (idx, buy) => {
        if(idx >= prices.length){
            return 0
        }
        if(cache[`${idx}i_${buy}b`]){
            return cache[`${idx}i_${buy}b`]
        }
        const res1 =  buy ? helper(idx+1, !buy) - prices[idx] : 0
        const res2 =  buy ? helper(idx+1, buy) : 0
        const res3 =  !buy ? helper(idx+1, !buy) + prices[idx] : 0
        const res4 =  !buy ? helper(idx+1, buy) : 0
        const result = Math.max(res1, res2 ,res3, res4)
        cache[`${idx}i_${buy}b`] = result
        return result
    }
    return helper(0, true)
};