from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        res = 0
        queue = [(root, str(root.val))]
        while queue:
            node, val = queue.pop(0)
            if not node.left and not node.right:
                res += int(val)
            else:
                if node.left:
                    valleft=node.left.val
                    queue.append((node.left, val+str(valleft)))
                if node.right:
                    valright=node.right.val
                    queue.append((node.right, val+str(valright)))
        return res


t3 = TreeNode(3)
t6 = TreeNode(2)
t7 = TreeNode(1, t3, t6)
solution = Solution()
result = solution.sumNumbers(t7)
assert result == 25