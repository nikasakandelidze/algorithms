class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=""
        for i in range(0,len(s)):
            j=0
            current=s[i]
            while i-j>=0 and i+j<len(s):
                b=False
                if i-j>=0:
                    prev=s[i-j]
                if i+j<len(s):
                    nxt=s[i+j]
                if prev == nxt:
                    string=s[i-j:j+i+1]
                else:
                    b=True
                if len(string) > len(res):
                    res=string
                if b:
                    break
                j+=1
            l=0
            r=1
            while i-l>=0 and i+r<len(s):
                b=False
                if i-l>=0:
                    prev=s[i-l]
                if i+r<len(s):
                    nxt=s[i+r]
                if prev == nxt:
                    string=s[i-l:i+r+1]
                else:
                    b=True
                if len(string) > len(res):
                    res=string
                if b:
                    break
                l+=1
                r+=1
        return res