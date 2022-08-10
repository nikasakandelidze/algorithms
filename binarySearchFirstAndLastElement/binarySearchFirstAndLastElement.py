class Solution:
    def _findPoint(self, nums, target, delta_x):
        if len(nums) == 0:
            return -1
        start = 0
        end = len(nums) - 1
        result = -1
        while start <= end:
            curr = (start + end) // 2
            if nums[curr] == target:
                new_curr = curr + delta_x
                if new_curr >= 0 and new_curr < len(nums) and nums[new_curr] == target:
                    if delta_x > 0:
                        start = curr + delta_x
                    else:
                        end = curr + delta_x
                else:
                    result = curr
                    break
            else:
                if nums[curr] < target:
                    start = curr + 1
                elif nums[curr] > target:
                    end = curr - 1
        return result

    def searchRange(self, nums, target: int):
        left = self._findPoint(nums, target, -1)
        right = self._findPoint(nums, target, 1)
        return [left, right]

solution = Solution()
result = solution.searchRange([1,1,2,3], 1)
assert result == [0,1]