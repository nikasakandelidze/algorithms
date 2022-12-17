from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if len(token) == 1 and not token.isnumeric():
                a = stack.pop()
                b = stack.pop()
                temp = None
                if token == "+":
                    temp = a + b
                elif token == "*":
                    temp = int(a * b)
                elif token == "/":
                    temp = int(b / a)
                elif token == "-":
                    temp = b - a
                stack.append(temp)
            else:
                # is number
                stack.append(int(token))
        return stack[0]


tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
assert Solution().evalRPN(tokens)==22
