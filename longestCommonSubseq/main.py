class Solution:
    # [1, 2, 3, 1, 2, 1]
    # [10, 11, 12, 1, 2, 15]
    def lengthOfLIS(self, nums: List[int]) -> int:
        # pattern for dynamic programming
        dp = [1]*len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i]=max(dp[j]+1, dp[i])
        return max(dp)


