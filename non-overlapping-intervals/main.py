class Solution:
    # [[1,2],[2,3],[3,4],[1,3]]
    # Return minimum number of intervals to remove so that resulted intervals are non-overlapping
    #  [[1,3],[2,4],[3,9]]
    #
    #   
    #[[1,2],[1,3],[2,3],[3,4]]
    #[[1,10], [1,3], [5,7]]
    # [a,b] [c,d] overlap when: a>=c and b<=d and a<d
    # The main unknown: Overlapping logic between two intervals
    #      [a,b] [c,d] 
    #       a. c  d b
    #       b > c and d > a
    #  c >= a
    #   Can non neighbours overlap? 
    #       [1,10] [2,4] [5,8]
    #
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        prev_idx = 0
        current_idx = 1
        count = 0
        while current_idx < len(intervals):
            prev = intervals[prev_idx]
            curr = intervals[current_idx]
            if curr[1] <= prev[1] and curr[0] >= prev[0]:
                count += 1
                prev_idx = current_idx
            elif curr[1] > prev[1] and curr[0] < prev[1]:
                count += 1
            else:
                prev_idx = current_idx
            current_idx += 1
        return count
           
