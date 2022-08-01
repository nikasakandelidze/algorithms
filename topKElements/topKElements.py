import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> List[int]:
        mins = []
        for x in nums:
            if len(mins) < k:
                heapq.heappush(mins, x)
            else:
                if mins[0] < x:
                    heapq.heappop(mins)
                    heapq.heappush(mins, x)
        return mins


# check
solution = Solution()

data = [3,2,1,5,6,4]
k=2
res = solution.findKthLargest(data, k)
assert 5 in res
assert 6 in res
assert len(res) == 2

data = [3,2,3,1,2,4,5,5,6]
k=4
res = solution.findKthLargest(data, k)
assert 5 in res
assert 6 in res
assert 4 in res
fives = list(filter(lambda x: x == 5, res))
assert len(fives) == 2
assert len(res) == 4
