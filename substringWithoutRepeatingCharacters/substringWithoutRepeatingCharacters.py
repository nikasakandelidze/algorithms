
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        resultLength = 0
        currentLength = 0
        seen = {}
        for idx, ch in enumerate(s):
            if ch not in seen:
                currentLength += 1
            else:
                resultLength = max(currentLength, resultLength)
                currentLength = idx - seen[ch]
                start = seen[ch]
                seen.clear()
                for j in range(start + 1, idx):
                    seen[s[j]] = j
            seen[ch] = idx
        resultLength = max(currentLength, resultLength)
        return resultLength
