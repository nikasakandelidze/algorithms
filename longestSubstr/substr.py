class Solution:
    #   Possible inputs (don't forget edge and complex  cases)
    #       Empty string
    #       String with only one character
    #       String with all the same characters
    #       String with capital and non-capital letters
    #       abcdefgat - character repeating is not at the end
    #       bcdefgaat - character repeating is at the end
    #       bcdaefgat - character repeating is in the middle   
    #
    #   Problem Statement:
    #       Find the longest substring without repeating characters in it
    #
    #   Potential solution:
    #       create some buffer to store set of chars S used in the currently active substring
    #       Start iterating character by character:
    #           if character is not in S:
    #               use this character as a substring
    #           if character is in S:
    #               we must stop looking at the current substring and should get ready for the next one.
    #
    #   Input: abcdefgat
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        total_result=0
        for i,ch in enumerate(s):
            if ch in chars:
                total_result=max(len(chars)//2, total_result)
                startIdx=chars[ch]
                new_chars={}
                for j in range(startIdx+1, i):
                    if j in chars:
                        new_chars[j]=chars[j]
                        new_chars[chars[j]]=j
                chars=new_chars
                chars[i]=ch
                chars[ch]=i
            else:
                chars[ch]=i
                chars[i]=ch
        return max(total_result, len(chars)//2)
