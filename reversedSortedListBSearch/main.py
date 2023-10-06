class Solution:
    # [4,5,6,7,0,1,2] pivot should be 4
    #   left = 0, right = 6
    #
    def find_pivot_index(self, nums):
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right)//2
            element = nums[mid]
            left_most = nums[left]
            prev = None if mid == 0 else nums[mid-1]
            nxt = None if mid == len(nums)-1 else nums[mid+1]
            if nxt is None:
                if prev > element:
                    return mid + 1
                else:
                    return -1
            if prev is None:
                if nxt < element:
                    return mid + 1
                else:
                    return -1
            if  nxt > element > prev:
                if prev > left_most:
                    left = mid + 1
                elif prev < left_most:
                    right = mid - 1
                else:
                    return -1
            elif prev > element:
                return mid
            elif nxt < element:
                return mid+1
        return -1

    def binary_search(self, nums, target, left, right):
        while left <= right:
            mid = (left+right)//2
            element = nums[mid]
            if element == target:
                return mid
            elif element > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        pivot_idx = self.find_pivot_index(nums) if len(nums)>1 else -1
        if pivot_idx == -1:
            return self.binary_search(nums, target, 0, len(nums)-1)
        else:
            left_result = self.binary_search(nums, target, 0, pivot_idx)
            if left_result != -1:
                return left_result
            right_result = self.binary_search(nums, target, pivot_idx, len(nums)-1)
            return right_result
       
