def bsearchForBreakpoint(nums, target):
    def search(start, end):
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1

    def searchForBreakpoint():
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            prev = nums[mid - 1] if mid > 0 else None
            nxt = nums[mid + 1] if mid < len(nums)-1 else None
            if prev is not None and prev > nums[mid]:
                return mid
            if nxt is not None and nxt < nums[mid]:
                return mid+1
            else:
                if nums[mid] < nums[start]:
                    end = mid - 1
                else:
                    start = mid + 1
        return -1

    if len(nums) == 1:
        return 0 if nums[0] == target else -1
    secondArrayStart = searchForBreakpoint()
    if secondArrayStart != -1:
        res1 = search(0, secondArrayStart - 1)
        if res1 != -1:
            return res1
        res2 = search(secondArrayStart, len(nums) - 1)
        if res2 != -1:
            return res2
        return -1
    else:
        return search(0, len(nums) - 1)

print(bsearchForBreakpoint([5,1,2,3,4], 3))
print(bsearchForBreakpoint([3,4,5,1,2], 3))
print(bsearchForBreakpoint([1,2,3,4,5], 3))
print(bsearchForBreakpoint([2,3,4,5,1], 3))
print(bsearchForBreakpoint([4,5,6,7,0,1,2], 0))
print(bsearchForBreakpoint([5,1,3], 1))
