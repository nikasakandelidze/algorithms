class Solution:
    # We are given numbers in an array
    # Each number has a sign for each neighbouring pair of nubers
    # if left one has positive sign and right one has negative sign largest sized one will be left only
    #   [10, -11, -11, 5]
    #
    #   Several potnetial cases for neighbouring pairs [......, a, b, ......]:
    #       a > 0  and b < 0 leave only bigger sized one
    #       a > 0 and b > 0 move forward to see other numbers
    #       a < 0 and b > 0 nothing since they go opposite sides
    #       a < 0 and b < 0 nothing for now
    #
    #   problem with hurrying and not understanding the problem and all possible inputs fully
    # 
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):
            current = asteroids[i]
            if not len(stack):
                stack.append(current)
            elif current < 0:
                if stack[-1] < 0:
                    stack.append(current)
                else:
                    add = False
                    while len(stack) and stack[-1] > 0:
                        if abs(stack[-1]) == abs(current):
                            add = False
                            stack.pop()
                            break
                        elif abs(stack[-1]) > abs(current):
                            add = False
                            break
                        elif abs(stack[-1]) < abs(current):
                            add = True
                            stack.pop()
                    if (not len(stack) or stack[-1] < 0) and add:
                        stack.append(current)
            else:
                stack.append(current)
        return stack
                

