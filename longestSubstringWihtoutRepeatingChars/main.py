class Solution:
    #   abcaiqweoiqjweoiqwjeoiqjweoiqwjeoiqwjeoij
    #
    #
    #   "qwecvew"  
    #
    #
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        result = 0
        last_start_idx=0
        for i in range(len(s)):
            ch = s[i]
            if ch in seen:
                idx=seen[ch]
                result = max(result, len(seen)//2)
                for j in range(last_start_idx, idx+1):
                    if j in seen:
                        ch2=seen[j]
                        del seen[j]
                        del seen[ch2]
                    last_start_idx = j
            seen[ch]=i
            seen[i]=ch
        return max(result, len(seen)//2)
