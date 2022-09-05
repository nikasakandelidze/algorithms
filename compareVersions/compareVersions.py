class Solution:
    #   Split both versions on .-s
    #       whichever is longer start iterating it
    #       if i-th element is not present on the second version compare i-th element of first version and 0
    #
    #
    #
    def compareVersion(self, version1: str, version2: str) -> int:
        v1Split = version1.split(".")
        v2Split = version2.split(".")
        toAddV2 = len(v1Split) - len(v2Split)
        toAddV1 = len(v2Split) - len(v1Split)
        if toAddV2 > 0:
            v2Split += toAddV2 * [0]
        elif toAddV1 > 0:
            v1Split += toAddV1 * [0]
        for i in range(len(v1Split)):
            first = int(v1Split[i])
            second = int(v2Split[i])
            if first < second:
                return -1
            elif first > second:
                return 1
            else:
                continue
        return 0

