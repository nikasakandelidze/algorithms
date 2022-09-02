from typing import List

# https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return abs(nums[0])
        currentSum = 0
        maxSum = float('-inf')
        for i in range(len(nums)):
            element = nums[i]
            if currentSum < 0:
                currentSum = element
            else:
                currentSum = currentSum + element
            if currentSum > maxSum:
                maxSum = currentSum
        currentSum = 0
        minSum = float('inf')
        for i in range(len(nums)):
            element = nums[i]
            if currentSum > 0:
                currentSum = element
            else:
                currentSum = currentSum + element
            if currentSum < minSum:
                minSum = currentSum

        return max(abs(maxSum), abs(minSum))
