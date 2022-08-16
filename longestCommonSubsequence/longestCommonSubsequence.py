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


res = longestCommonSubsequence("", "")
assert res == 0

res = longestCommonSubsequence("qwe", "qwe")
assert res == 3

res = longestCommonSubsequence("qwe", "qe")
assert res == 2

res =longestCommonSubsequence("zxcqwe", "zce")
assert res == 3


