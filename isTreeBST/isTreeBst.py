# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def helper(lower, upper, root):
            if root is None:
                return True
            if root.val > lower and root.val < upper:
                return helper(lower, min(root.val, upper), root.left) and helper(max(root.val, lower), upper,
                                                                                 root.right)
            return False

        return helper(float('-inf'), float('inf'), root)
