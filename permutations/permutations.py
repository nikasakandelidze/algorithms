
# https://leetcode.com/problems/permutations/
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1 or len(nums) == 0:
            return [nums]
        temp = []
        for i in range(len(nums)):
            res = self.permute(nums[0:i] + nums[i + 1:])
            for r in res:
                temp.append(r + [nums[i]])
        return temp

