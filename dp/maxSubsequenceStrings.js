/**
 * @param {string} text1
 * @param {string} text2
 * @return {number}
 */
/*
    [a, ab, ac, abc, ad, abd, acd]
    Brute Force Strategy:
        - Generate all possible subsequences for both of the strings //O(2^N)
        - Determine the longest common subsequence
 */
var longestCommonSubsequence = function(text1, text2) {
    const dp = Array.from(Array(text1.length+1), x=>Array(text2.length+1))
    dp[0].fill(0)
    dp.forEach(arr=>{arr[0]=0})
    for(let i=1; i<dp.length; i++){
        for(let j=1; j<dp[i].length; j++){
            if(text1[i-1]===text2[j-1]){
                dp[i][j]=1+dp[i-1][j-1]
            }else{
                dp[i][j]=Math.max(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])
            }
        }
    }
    return dp[text1.length][text2.length]
};