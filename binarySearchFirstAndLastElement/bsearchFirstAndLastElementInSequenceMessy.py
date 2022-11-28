class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]

        def findFirstIndex():
            start = 0
            end = len(nums) - 1
            while start <= end:
                mid = (start + end) // 2
                pivot = nums[mid]
                if pivot > target:
                    end = mid - 1
                elif pivot < target:
                    start = mid + 1
                else:
                    if mid == 0:
                        return mid
                    else:
                        prevPivot = nums[mid - 1]
                        if prevPivot == pivot:
                            end = mid - 1
                        else:
                            return mid
            if start == end:
                return -1 if nums[start] != target else start
            return -1

        def findLastIndex():
            start = 0
            end = len(nums) - 1
            while start <= end:
                mid = (start + end) // 2
                pivot = nums[mid]
                if pivot > target:
                    end = mid - 1
                elif pivot < target:
                    start = mid + 1
                else:
                    if mid == len(nums) - 1:
                        return mid
                    else:
                        prevPivot = nums[mid + 1]
                        if prevPivot == pivot:
                            start = mid + 1
                        else:
                            return mid
            if start == end:
                return -1 if nums[start] != target else start
            return -1

        return [findFirstIndex(), findLastIndex()]
