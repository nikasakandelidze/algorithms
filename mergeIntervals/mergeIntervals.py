class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x:x[0])
        result = []
        curr = []
        for x in intervals:
            if not curr:
                curr = x
            else:
                if x[0] <= curr[1]:
                    curr[1] = max(x[1], curr[1])
                else:
                    result.append(curr)
                    curr = x
        if curr:
            result.append(curr)
        return result


solution = Solution()
result = solution.merge([[1,2], [3,6], [5,10], [7,8]])
print(result)