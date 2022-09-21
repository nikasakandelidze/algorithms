def dpLongestCommonSubstring(text1, text2):
    dp = [[0 for _ in range(len(text1) + 1)] for _ in range(len(text2) + 1)]
    result=float('-inf')
    for i in range(1, len(dp)):
        for j in range(1, len(dp[i])):
            if text2[i - 1] == text1[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                result=max(result,dp[i][j])
            else:
                dp[i][j] = 0
    return result if result != float('-inf') else 0


def recursiveLongestCommonSubstring(text1, text2):
    def helper(s1,s2,idx1,idx2, match):
        if len(s1)-1 < idx1 or len(s2)-1 < idx2:
            return 0
        res = float('-inf')
        if s1[idx1] == s2[idx2]:
            res = 1 + helper(s1, s2, idx1 + 1, idx2 + 1, True)
        if match:
            return 0 if res == float('-inf') else res
        res1 = helper(s1, s2, idx1+1, idx2, False)
        res2 = helper(s1, s2, idx1, idx2+1, False)
        return max(res1, res2, res)
    return helper(text1, text2, 0, 0, False)


print(dpLongestCommonSubstring("", ""))
print(recursiveLongestCommonSubstring("", ""))
print(dpLongestCommonSubstring("a", "aac"))
print(recursiveLongestCommonSubstring("a", "aac"))
print(dpLongestCommonSubstring("baa", "aac"))
print(recursiveLongestCommonSubstring("baa", "aac"))
print(dpLongestCommonSubstring("abaa", "aaca"))
print(recursiveLongestCommonSubstring("abaa", "aaca"))
print(dpLongestCommonSubstring("abaatqqqqq", "aaqqqqqca"))
print(recursiveLongestCommonSubstring("abaatqqqqq", "aaqqqqqca"))
