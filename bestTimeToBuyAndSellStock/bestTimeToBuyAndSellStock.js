/**
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
 */
var maxProfit = function(prices) {
    const getNextAction =(action)=>{
        if(action==='BUY'){
            return 'SELL'
        }else if(action ==='SELL'){
            return 'COOLDOWN'
        }else {
            return 'BUY'
        }
    }
    const cache ={}
    const helper = (pricesArray, action, idx) => {
        if(idx >= pricesArray.length){
            return 0
        }
        if(cache[`${action}${idx}`]) return cache[`${action}${idx}`]
        const current = action==='SELL' ? pricesArray[idx] : action==='BUY' ? -1*pricesArray[idx] : 0
        const nextAction=getNextAction(action)
        const temp1 = current + helper(pricesArray, nextAction, idx+1)
        const temp2 = helper(pricesArray, action, idx+1)
        const result = Math.max(temp1, temp2)
        cache[`${action}${idx}`]=result
        return result
    }
    return helper(prices, 'BUY', 0)
};