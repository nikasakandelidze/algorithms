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

/*
    abcde
    ace
*/
var longestCommonSubsequenceTopDown = function(text1, text2) {
    const cache = {}
    const helper = (i,j) => {
        if(i >= text1.length || j >= text2.length){ 
            return 0
        }
        if(cache[`${i}i_${j}j`]){
            return cache[`${i}i_${j}j`]
        }
        const ch1 = text1[i]
        const ch2 = text2[j]
        if(ch1===ch2){
            const res = 1 + helper(i+1,j+1)
            cache[`${i}i_${j}j`] = res
            return res
        }else{
            const res = Math.max(helper(i+1,j), helper(i+1,j+1), helper(i,j+1))
            cache[`${i}i_${j}j`] = res
            return res
        }
    }
    return helper(0,0)
}