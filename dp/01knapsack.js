/*
    So when building a 2 dimensional array over here two axis-es are:
        - items: result up to i-th item including 
        - weight: what's the solution for the weight w(0-capacity)


    So the idea of the bottom up solution is to start considering from 0-capacity and from 1st to all inclusive items,
    this way at first solve only smaller problems ( like what if there was only 1 item and capacity was 1 and etc, then what if we increase capacity)
*/
const knapsack = (items, capacity) => {
    const dp = Array(items.length+1).fill(Array(capacity+1))
    dp[0].fill(0)
    for(let i=0; i<=items.length; i++){
        dp[i][0] = 0
    }
    /*
        These nested loops are for iterating on all possible cases of:
            capacity - from 0 to Capacity
            items - from item1 to set of all items included
        Meaning that there will be all the case of capacity from 0-j on j-th iteration, thus j-item.weight for any possible case will already be solved.
        
    */
    for (let i=1; i<dp.length; i++){
        for (let j=1; j<dp[i].length; j++){
            if(items[i-1].weight > j){
                dp[i][j] = dp[i-1][j]
            }else{
                dp[i][j] = Math.max(dp[i-1][j], items[i-1].cost + dp[i-1][j-items[i-1].weight])
            }
        }
    }
    return dp[items.length][capacity]
}