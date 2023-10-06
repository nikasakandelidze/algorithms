class Solution:
    #   It looks to me like a recursive problem
    #   well-formed parentheses: every opened parentheses should have a corresponding closed one
    #   while we have open or closed parentheses left drain them
    #
    def generateParenthesis(self, n):
        def recursive(open_count, close_count, s):
            if open_count == 0 and close_count == 0:
                return [s]
            open_result = recursive(open_count-1, close_count+1, s+'(') if  open_count > 0 else []
            close_result = recursive(open_count, close_count-1, s+')') if  close_count > 0 else []
            return open_result + close_result
        return recursive(n, 0, "")

result = Solution().generateParenthesis(3)
print(result)