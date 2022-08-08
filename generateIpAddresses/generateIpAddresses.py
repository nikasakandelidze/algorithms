class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self._recursive(s, 0, res, "", 4)
        return res

    def _isIpAddressValid(self, ipAddress):
        parts = ipAddress.split(".")
        if len(parts) < 4:
            return False
        for p in parts:
            if p == "":
                return False
            if int(p) > 255 or (len(p) > 1 and p[0] == '0'):
                return False
        return True

    def _recursive(self, s, idx, res, new_s, dots):
        if dots == 0 or idx >= len(s):
            if (self._isIpAddressValid(new_s)):
                res.append(new_s)
        else:
            self._recursive(s, idx + 1, res, new_s + s[idx], dots)
            self._recursive(s, idx + 1, res, new_s + s[idx] + ".", dots - 1)


solution = Solution()
result = solution.restoreIpAddresses("123123123123")
print(result)
assert len(result) == 1