from typing import List


class Solution:
    def buildPrefixProduct(self, nums):
        result = [-1 for _ in range(len(nums))]
        result[0] = 1
        for i in range(1, len(nums)):
            result[i] = result[i - 1] * nums[i - 1]
        return result

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = self.buildPrefixProduct(nums)
        m = self.buildPrefixProduct(nums[-1::-1])[-1::-1]
        result = []
        for i in range(0, len(nums)):
            result.append(n[i] * m[i])
        return result