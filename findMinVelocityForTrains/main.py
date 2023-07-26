import math

class Solution:
    #   Technically this problem boils down to the formula: V=S/T but still not exactly,
    #   since it would have been an answer in case of having non-delayed times between trains
    #   now since in the problem statement it's written that there might easily be delays between
    #   trains because of non-integer valued times needed person will need to wait for a next bigger integer to appear.
    #
    #   start from v_current = 1
    #   while True:
    #       times = [float(x)/v_current for x in dist]
    #       fill_non_integer_values_to_their_next_bigger_int(times)
    #       total_time = sum(times)
    #       if total_time <= hour:
    #           return v_current
    #       if total_time > hour:
    #
    #       delta_factor = hour/total_time
    #       v_current *= delta_factor
    #
    #
    #   [1,3,2] 3.15
    #   v_current=2.22 -> 0.3 + 0.95 + 0.63 = 1.88
    #
    #
    #
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def get_total_time_for_v(v):
            times = [float(x)/v for x in dist]
            for i in range(len(times)-1):
                times[i]=math.ceil(times[i])
            return sum(times)
        left = 1
        right = 10**7
        result = float('inf')
        while left <= right:
            mid = (right + left)//2
            potential_time = get_total_time_for_v(mid)
            if potential_time <= hour:
                if mid < result:
                    result = mid
                right = mid - 1
            elif potential_time > hour:
                left = mid + 1
        return result if result != float('inf') else -1