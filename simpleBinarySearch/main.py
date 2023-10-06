class Solution:
    #   [1,2,3,4]
    #   [1,2,3,4,5]
    #
    #
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right)//2
            element = nums[mid]
            if element == target:
                return mid
            elif element > target:
                right = mid -1
            else:
                left = mid + 1
        return -1