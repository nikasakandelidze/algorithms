def findMaxAverage(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """
    if len(nums) == 1:
        return float(nums[0])
    curr_sum = 0
    curr_len = 0
    curr_avg = (float('-inf'))
    for i in range(len(nums)):
        curr_len += 1
        curr_sum += nums[i]
        if i >= k - 1:
            if i >= k:
                curr_sum -= nums[i-k]
                curr_len -= 1
            new_avg = float(curr_sum) / curr_len
            if new_avg > curr_avg:
                curr_avg = new_avg
    return curr_avg


class Solution(object):
    pass


result = findMaxAverage([1,2,3,4,5,6], 2)
assert result == 5.5