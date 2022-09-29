# https://leetcode.com/problems/reverse-integer/
class Solution(object):
    maxValue = 2147483647

    def lengthOfNumber(self, x):
        res = 0
        while x > 0:
            res += 1
            x = x // 10
        return res

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        length = self.lengthOfNumber(x) - 1
        while x > 0:
            temp = x % 10
            res += temp * (10 ** length)
            length -= 1
            x = x // 10
            if res > Solution.maxValue:
                return 0
        return res * sign