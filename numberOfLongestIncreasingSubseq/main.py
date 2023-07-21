
class Solution:
    #   input array of numbers return longest increasing subsequence
    #   members of this subsequence don't have to be neighbouring
    #      
    #   It should be strictly increasing   
    #
    #   Algorithm #1:
    #       Top down approach with recursive dynamic programming    
    #
    #   [4,7]
    def findNumberOfLIS(self, nums: List[int]) -> int:
        @cache
        def recursiveLIS(idx, prev_element):
            if idx == len(nums):
                return [1,1]
            current = nums[idx]
            res1 = [0,0]
            if prev_element is None or prev_element < current:
                res1 = recursiveLIS(idx+1, current)
            res2 = recursiveLIS(idx+1, prev_element)
            if res1[0]+1 > res2[0]:
                return [res1[0]+1, res1[1]]
            elif res1[0]+1 == res2[0]:
                return [res1[0]+1, res1[1] + res2[1]]
            elif res1[0]+1 < res2[0]:
                 return [res2[0], res2[1]]
        return recursiveLIS(0, None)[1]

