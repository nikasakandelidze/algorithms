class Solution:
    #   Given an array on numbers give the length of longest non-empty subarray of 1-s if you can delete 1 element
    #   if delete wasn't the case simply getting the longest subarray of 1-s is next:
    #       iterate over the whole array and for each element:
    #           if it's one and previous element was also one:
    #               increase temp counter
    #           if it's one and previous element was not one:
    #               increase temp counter
    #           if it's not one and previous was one:
    #               reset temp counter 
    #           if it's not one and previous was also not one:
    #               skip
    #
    #
    #    [1,1,0,1]
    def longestSubarray(self, nums):
        result = 0
        temp_result = 0
        deleted = False
        is_non_1_present = any((lambda x: x!=1)(num) for num in nums)
        after_deletion_count=0
        for num in nums:
            if num == 1 and temp_result >= 0:
                temp_result += 1
                if deleted:
                    after_deletion_count += 1
            elif num != 1 and temp_result > 0:
                if not deleted:
                    deleted = True
                    continue
                else:
                    result=max(temp_result, result)
                    temp_result=0
                    deleted = False
                    if after_deletion_count > 0:
                        temp_result = after_deletion_count
                        after_deletion_count = 0
                        deleted = True
        if temp_result > 0:
            result = max(temp_result, result)
        return result if is_non_1_present else result-1

print(Solution().longestSubarray([0,1,1,1,0,1,1,0,1,1,1,1,1,1,1]))
