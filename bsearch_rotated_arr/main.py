class Solution:
    #   After the potential rotation, array is split into 2 parts and both of them are in an ascending order
    #   but they are not sorted in respect to one another.
    #
    # [5,6,7,1,2,3,4]
    #   After choosing the middle index there are 3 different possibilities:
    #       1) Either mid is fully in left ascending sub array
    #       2) Either mid is fully in the right ascending sub array
    #       3) Either mid is on the edge of left and right asecnding sub arrays
    #   In all of these cases we should act accordingly.
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1

        def bsearch(start, end):
            l = start
            r = end
            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return -1

        res = bsearch(0, left - 1)
        if res != -1:
            return res
        res = bsearch(left, len(nums) - 1)
        return res