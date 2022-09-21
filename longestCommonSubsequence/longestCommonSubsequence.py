# This algorithm is used in git diff mechanism
# General mechanism that we can take from here is that if we work with algorithm that has 2 strings as inputs
# memoization using two dimensional array would be cool, to track computational result on memo[idx1][idx2] of strings.

def longestCommonSubsequence(text1, text2):
    def helper(text1, text2, idx1, idx2, memo):
        if idx1 >= len(text1) or idx2 >= len(text2):
            return 0
        if memo[idx1][idx2] != -1:
            return memo[idx1][idx2]
        if text1[idx1] == text2[idx2]:
            result = 1 + helper(text1, text2, idx1+1, idx2+1, memo)
            memo[idx1][idx2] = result
            return result
        else:
            first_result = helper(text1, text2, idx1 + 1, idx2, memo)
            second_result = helper(text1, text2, idx1, idx2 + 1, memo)
            result = max(first_result, second_result)
            memo[idx1][idx2] = result
            return result
    memo = [[-1 for _ in text2] for _ in text1]
    return helper(text1, text2, 0, 0, memo)


# if we have a tabular solution for dynamic programming problem it's usually much easier to implement maximization solution than a minimization one
# since for maximization we can easily initialize matrix to 0-s
def dpLongestCommonSubsequence(text1, text2):
    dp=[[0 for _ in range(len(text1)+1)] for _ in range(len(text2)+1)]
    for i in range(1,len(dp)):
        for j in range(1,len(dp[i])):
            if text2[i-1]==text1[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]


res = longestCommonSubsequence("", "")
res2 = dpLongestCommonSubsequence("","")
assert res == 0
assert res2 == 0

res = longestCommonSubsequence("qwe", "qwe")
res2 = dpLongestCommonSubsequence("qwe","qwe")
assert res == 3
assert res2 == 3

res = longestCommonSubsequence("qwe", "qe")
res2 = dpLongestCommonSubsequence("qwe", "qe")
assert res == 2
assert res2 == 2

res =longestCommonSubsequence("zxcqwe", "zce")
res2 =dpLongestCommonSubsequence("zxcqwe", "zce")
assert res == 3
assert res2 == 3


