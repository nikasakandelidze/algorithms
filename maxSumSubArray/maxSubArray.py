from typing import List


# https://leetcode.com/problems/maximum-subarray/
class Solution:
    def buildPrefixSum(self, nums):
        prefixSums = [-1 for _ in range(len(nums) + 1)]
        prefixSums[len(prefixSums) - 1] = nums[-1]
        for i in range(len(nums)):
            if i == 0:
                prefixSums[i] = nums[i]
            else:
                if prefixSums[i - 1] >= 0:
                    prefixSums[i] = prefixSums[i - 1] + nums[i]
                else:
                    prefixSums[i] = nums[i]
        return prefixSums

    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        prefixSums = self.buildPrefixSum(nums)
        return max(prefixSums)

