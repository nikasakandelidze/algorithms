MAX_INT_VAL = 2147483647
MIN_INT_VAL = 2147483648


class Solution:
    def extractNumericPartOfString(self, s: str) -> str:
        res = ""
        for ch in s:
            if (ch == '-' or ch == '+') and not res:
                continue
            if ch.isnumeric():
                res += ch
            else:
                break
        return res

    def numericStringToNum(self, s: str, minus: bool) -> int:
        result = 0
        power = 0
        s = s[-1::-1]
        for ch in s:
            if not ch.isnumeric():
                break
            n = int(ch)
            result += n * (10 ** power)
            if not minus:
                if result >= MAX_INT_VAL:
                    return MAX_INT_VAL
            if minus:
                if result >= MIN_INT_VAL:
                    return MIN_INT_VAL
            power += 1
        return result

    def checkForDuplicateSigns(self, s: str) -> bool:
        seen = False
        seenNumeric = False
        for ch in s:
            if ch == '-' or ch == '+':
                if seen and not seenNumeric:
                    return True
                else:
                    seen = True
            elif ch.isnumeric():
                seenNumeric = True
        return False

    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if s == "" or self.checkForDuplicateSigns(s):
            return 0
        sign = -1 if s[0] == '-' else 1
        return sign * self.numericStringToNum(self.extractNumericPartOfString(s), sign == -1)