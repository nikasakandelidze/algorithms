from typing import List


class Solution:
    # sort array
    # start iterating one by one
    # for each iteration reiterate(to right) the rest of array
    #   for each element
    #
    # [-4, -1, -1, 0, 1, 2]
    # x + y + z = 0
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        res = []
        nums.sort()
        for i in range(len(nums) - 1):
            data = {}
            current = nums[i]
            for j in range(i + 1, len(nums)):
                nextOne = nums[j]
                if nextOne in data:
                    temp = data[nextOne][:]
                    temp.append(nextOne)
                    if tuple(temp) not in visited:
                        visited.add(tuple(temp))
                        res.append(temp)
                else:
                    key = -1 * (current + nextOne)
                    data[key] = [current, nextOne]
        return res


