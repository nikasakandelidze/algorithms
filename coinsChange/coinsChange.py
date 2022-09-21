from typing import List

# https://leetcode.com/problems/coin-change/submissions/
# The idea is exactly the same like for knapsack dynamic programming, bottom up solution.
# You need to solve smaller sub problems first and only then transition to bigger problems.


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize two dimensional array for amount and coins since for each of these coins
        # we'll need to make a choice to either include it in the final solution or not. We need to have matrix which let's us know whether we should do it or not.
        dp=[[float('inf') for _ in range(len(coins)+1)] for _ in range(amount+1)]
        # for 0 used coins value result value will always be 0
        for i in range(len(dp)):
            dp[i][0]=0
        # for 0 amount to get result value will always be 0
        for i in range(len(coins)+1):
            dp[0][i]=0
        for currAmount in range(1, len(dp)):
            for coinIdx in range(len(dp[currAmount])):
                currentCoin = coins[coinIdx-1]
                # If current coin that we are looking at is bigger then the amount we are trying to get to
                # it means that we can't incorporate this coin in our current solution and result for matrix's this elements will be
                # result of the previous solution for the same amount but for the coins except for the current one.
                if currentCoin > currAmount:
                    dp[currAmount][coinIdx]=dp[currAmount][coinIdx-1]
                else:
                    # if current coin fits in the target amount. Let's see if we choose this coin what other valued coin we can take with it.
                    # this will be calculated with currAmount-currentCoin
                    first=dp[currAmount-currentCoin][coinIdx]+1 # result value if we choose to take this current element
                    second=dp[currAmount][coinIdx-1] # result  value if we choose not to take this current element
                    dp[currAmount][coinIdx]=min(first,second) # since we are asked a minimization problem we must take min of 2 possible values
        return dp[-1][-1] if dp[-1][-1] != float('inf') else -1