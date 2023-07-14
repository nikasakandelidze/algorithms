    #   diff=2 [2,4,8,1,3,5,7,9,11,6,8,10,12,14,16,18,20]
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        values = {}
        for i in range(0, len(arr)):
            current = arr[i]
            prev=current-difference
            values[current]=values[prev]+1 if prev in values else 1
        return max(values.values())
